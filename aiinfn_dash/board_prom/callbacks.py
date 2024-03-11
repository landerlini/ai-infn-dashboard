import dash
import logging

from aiinfn_dash.auth import User

def register_callbacks(app):
    @app.callback(
        dash.Output('prom:title', 'children'),
        dash.Input('prom:my-input', 'value'),
    )
    def update_title(my_input):
        logging.info("Called update_title")
        with User.from_session() as user:
            return my_input.replace("%", f" {user.name} ") if '%' in my_input else f"{my_input} {user.name}"
    


    @app.callback(
        dash.Output('prom:title2', 'children'),
        dash.Input('prom:rosa-input', 'value'),
    )
    def update_title2(my_input):
        logging.info("Called update_title2")
        with User.from_session() as user:
            return (f"La tua password è: {my_input}")
