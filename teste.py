import dash
from dash import dcc, html 
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button('Adicionar Linha', id='add-row-button'),
        html.Div(
            [
                dcc.Input(id='campo-1', type='text', placeholder='Campo 1'),
                dcc.Input(id='campo-2', type='text', placeholder='Campo 2'),
                html.Button('Adicionar', id='submit-button')
            ],
            id='modal',
            style={'display': 'none'}
        ),
        html.Table(
            id='table',
            children=[
                html.Thead(
                    html.Tr(
                        [
                            html.Th('Coluna 1'),
                            html.Th('Coluna 2')
                        ]
                    )
                ),
                html.Tbody(
                    [
                        html.Tr(
                            [
                                html.Td('Valor 1'),
                                html.Td('Valor 2')
                            ]
                        ),
                        html.Tr(
                            [
                                html.Td('Valor 3'),
                                html.Td('Valor 4')
                            ]
                        )
                    ]
                )
            ],
            style={'margin': '20px'}
        )
    ]
)


@app.callback(
    Output('modal', 'style'),
    [Input('add-row-button', 'n_clicks')],
    [State('modal', 'style')]
)
def toggle_modal(n_clicks, style):
    if n_clicks:
        if style['display'] == 'none':
            style['display'] = 'block'
        else:
            style['display'] = 'none'
    return style


@app.callback(
    Output('table', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('campo-1', 'value'),
     State('campo-2', 'value'),
     State('table', 'children')]
)
def add_row(n_clicks, campo_1, campo_2, table):
    if n_clicks:
        new_row = html.Tr([html.Td(campo_1), html.Td(campo_2)])
        table[1]['props']['children'].append(new_row)
        return table
    return table


if __name__ == '__main__':
    app.run_server(debug=True)