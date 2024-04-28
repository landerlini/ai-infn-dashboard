from dash import html, dcc, dash_table


def layout():
    cols = ["A", "B", "C"]
    return html.Div([
            html.Div([
                html.Span("👤", className='user-logo'),
                html.Span(f"Username", className='user-name', id='user-name'),
            ], className="user-menu"),
            html.Div([
                html.H1(f'VK Dispatcher Dashboard', id='vkd:title', className='main-title'),
                dash_table.DataTable(data=[], columns=[{'name': c, 'id': c} for c in cols], id='status-table')
        ], className='data-table'),
        html.Div(
            [
                html.Span(
                    f"©️ AI_INFN 2024. Contribute to this dashboard on GitHub: ",
                    className='footer-message',
                ),
                html.A(
                    f"landerlini/ai-infn-dashboard",
                    href="https://github.com/landerlini/ai-infn-dashboard",
                    target='_blank',
                    className='footer-message',
                ),
            ], className='footer',
        )
    ])
