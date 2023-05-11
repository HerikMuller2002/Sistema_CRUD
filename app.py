import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State, ALL

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

options = [{'label': 'Opção 1', 'value': 1},
           {'label': 'Opção 2', 'value': 2},
           {'label': 'Opção 3', 'value': 3},
           {'label': 'Opção 4', 'value': 4},
           {'label': 'Opção 5', 'value': 5}]

dropdown = dbc.DropdownMenu(
    label='Selecione uma opção',
    children=[
        dbc.Input(id='dropdown-search', type='text', placeholder='Pesquisar...'),
        dbc.DropdownMenuItem(divider=True),
        *[dbc.DropdownMenuItem(option['label'], id={'type': 'dropdown-option', 'index': option['value']}) for option in options]
    ]
)

app.layout = html.Div([
    dropdown,
    html.Br(),
    html.Div(id='selected-option')
])


@app.callback(
    Output('dropdown-search', 'value'),
    [Input('dropdown-search', 'n_submit'), Input('dropdown-search', 'value')],
    prevent_initial_call=True
)
def clear_dropdown_search(n, value):
    if n:
        return value
    return ''


@app.callback(
    Output('dropdown-option', 'style'),
    [Input('dropdown-search', 'value')],
    [State({'type': 'dropdown-option', 'index': ALL}, 'id')],
    prevent_initial_call=True
)
def filter_options(search_value, option_ids):
    if not search_value:
        return {'display': 'block'}
    filtered_ids = [option_id for option_id in option_ids if options[option_id['index'] - 1]['label'].lower().startswith(search_value.lower())]
    return {'display': 'block'} if filtered_ids else {'display': 'none'}


@app.callback(
    Output('selected-option', 'children'),
    [Input({'type': 'dropdown-option', 'index': ALL}, 'n_clicks')],
    prevent_initial_call=True
)
def update_selected_option(n_clicks):
    for i, n in enumerate(n_clicks):
        if n:
            return f'Opção selecionada: {options[i]["label"]}'


if __name__ == '__main__':
    app.run_server(debug=True)