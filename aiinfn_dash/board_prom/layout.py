from dash import html, dcc


def layout():
    return html.Div([html.H1(f'Ciao, !', id='title'), dcc.Input(id='my-input', value='', type='text')])
