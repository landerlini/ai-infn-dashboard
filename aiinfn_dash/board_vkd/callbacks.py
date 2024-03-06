import dash
import logging

from aiinfn_dash.auth import User


def register_callbacks(app):
    @app.callback(
        dash.Output('vkd:title', 'children'),
        dash.Input('vkd:my-input', 'value'),
    )
    def vkd_update_title(my_input):
        logging.info("Called vkd update_title")
        with User.from_session() as user:
            return my_input.replace("%", f" {user.name} ") if '%' in my_input else f"{my_input} {user.name}"
