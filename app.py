import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

dropdown = dbc.DropdownMenu(
    [
        dbc.Label("Escolha uma opção"),
        dcc.Dropdown(
            id="my-dropdown",
            options=[
                {"label": "Opção 1", "value": "opcao1"},
                {"label": "Opção 2", "value": "opcao2"},
                {"label": "Opção 3", "value": "opcao3"},
            ],
            value=None,
        ),
    ]
)

app.layout = dbc.Container(
    [
        dropdown,
        html.Div(id="output-div")
    ]
)

@app.callback(Output("output-div", "children"), [Input("my-dropdown", "value")])
def update_output(value):
    if value is not None:
        return f"Você selecionou a opção {value}."
    else:
        return "Nenhuma opção selecionada."

if __name__ == "__main__":
    app.run_server(debug=True)