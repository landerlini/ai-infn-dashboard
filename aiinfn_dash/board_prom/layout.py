from dash import html, dcc


def layout():
    return html.Div([html.H1(f'Ciao, !', id='prom:title'), dcc.Input(id='prom:my-input', value='', type='text')])
