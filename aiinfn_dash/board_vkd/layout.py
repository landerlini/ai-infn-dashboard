from dash import html, dcc, dash_table


def layout():
    cols = ["A", "B", "C"]
    return html.Div([
        html.H1(f'Ciao, !', id='vkd:title'),
        dcc.Input(id='vkd:my-input', value='', type='text'),
        dash_table.DataTable(data=[], columns=[{'name': c, 'id': c} for c in cols])
    ])
