import dash
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Criação do DataFrame de exemplo
data = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'Idade': [25, 30, 35, 40],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília']
}
df = pd.DataFrame(data)

# Layout
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                dbc.Input(type="search", id="search-input", placeholder="Pesquisar"),
                width=6,
            ),
        ),
        dbc.Row(
            dbc.Col(
                html.Div(id="table-container"),
            ),
        ),
    ],
    fluid=True,
)

# Callback para filtrar a tabela
@app.callback(
    Output("table-container", "children"),
    Input("search-input", "value")
)
def filter_table(search_value):
    if search_value is None:
        filtered_df = df
    else:
        filtered_df = df[df['Nome'].str.contains(search_value, case=False)]
    
    table = dbc.Table.from_dataframe(filtered_df, striped=True, bordered=True, hover=True)
    return table

if __name__ == '__main__':
    app.run_server(debug=True)