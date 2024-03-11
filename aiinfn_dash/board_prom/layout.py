from dash import html, dcc


def layout():
    return html.Div([
        html.H1(f'Ciao, !', id='prom:title'), 
        dcc.Input(id='prom:my-input', value='', type='text'),
        html.H1(f'Ciao, !', id='prom:title2'),
        dcc.Input(id='prom:rosa-input', value='', type='password')
        ])
    

