from flask import Flask, session as flask_session
import dash
import logging
import waitress
from . import configuration as cfg
from .auth import configure_authentication

# Import dashboards
import aiinfn_dash

server = Flask(__name__)
server.config.update(
    OIDC_REDIRECT_URI=cfg.IAM_REDIRECT_URI,
    SECRET_KEY=cfg.FLASK_SECRET,
)
auth = configure_authentication(server)

# Register dashboards
__dashboards__ = {
    k: dash.Dash(
        f"{__name__}-{k}",
        server=server,
        url_base_pathname=f"/dash/{k}/",
    ) for k in ('prom', 'vkd')
}

for dashboard, dash_app in __dashboards__.items():
    dash_app.layout = getattr(aiinfn_dash, f"board_{dashboard}").layout()
    getattr(aiinfn_dash, f"board_{dashboard}").register_callbacks(dash_app)

for view_func in server.view_functions:
    for dash_app in __dashboards__.values():
        if view_func.startswith(dash_app.config['url_base_pathname']):
            server.view_functions[view_func] = auth.access_control('default')(server.view_functions[view_func])


@server.route('/logout')
@auth.oidc_logout
def logout():
    return "You've been successfully logged out!"


if __name__ == '__main__':
    log_format = '%(asctime)-22s %(name)-10s %(levelname)-8s %(message)-90s'
    logging.basicConfig(
        format=log_format,
        level=logging.DEBUG if cfg.DEBUG else logging.INFO,
    )

    if cfg.DEBUG:
        server.run(
            debug=True,
            host=cfg.HOST,
            port=cfg.PORT,
            # For signing your certificate, refer to https://kracekumar.com/post/54437887454/ssl-for-flask-local-development/
            #ssl_context=('server.crt', 'server.key'),
        )
    else:
        waitress.serve(server, host=cfg.HOST, port=cfg.PORT)
