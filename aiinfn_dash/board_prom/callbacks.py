import dash
import logging

from aiinfn_dash.auth import User

@dash.callback(
    dash.Output('title', 'children'),
    dash.Input('my-input', 'value'),
)
def update_title(my_input):
    logging.info("Called update_title")
    with User.from_session() as user:
        return user.name
