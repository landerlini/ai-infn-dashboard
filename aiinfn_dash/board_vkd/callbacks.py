import dash
import logging

from aiinfn_dash.auth import User


def register_callbacks(app):
    @app.callback(
        dash.Output('user-name', 'children'),
        dash.Input('status-table', 'value'),
    )
    def vkd_update_title(my_input):
        logging.info("Called vkd update_title")
        with User.from_session() as user:
            return user.name
