import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output, State

import sys
import os
import json
from datetime import datetime

diretorio_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, diretorio_pai)
from project.database.account import *

# app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP,r'/assets/css/Login.css'])
# app.title = 'Login'

df = importar_tabela('project\\database\\banco.db', 'problemas')
try:
    df = df.drop(['description','link'], axis=1)
except KeyError:
    pass
df.astype(str)
df = df.applymap(lambda x: x.lower().capitalize() if isinstance(x, str) else x)


# app.layout = html.Div([
#         dash_table.DataTable(
#             df.to_dict('records'),
#             columns=[{"name": i, "id": i} for i in df.columns],
#             id='table_id',
#             style_header={
#                 'backgroundColor': '#1c273c',
#                 'color': 'white',
#                 'font-weight': 'bold',
#                 'font-size':'1.2rem',
#                 'textAlign': 'left',
#                 'padding': '8px',
#                 'position': 'sticky',
#                 'top': '0',
#                 'z-index': '1',
#                 'border': '2px solid #141c2b',
#                 'border-top': '0',

#             },
#             style_data={
#                 'backgroundColor': '#293751',
#                 'color': 'white',
#                 'textAlign': 'left',
#                 'border': '2px solid #141c2b',
#                 'padding': '8px',
#                 'font-size':'1rem'
#             },
#             style_table={
#                 'padding': '0', 
#                 'margin': '0', 
#                 'height':'85vh',
#                 'width':'83vw',
#                 'overflowY': 'scroll',
#                 'overflowX': 'scroll',
#                 'font-family': 'Roboto'
#                 }
#         )
# ])

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='adding-rows-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        # coluna fixa
            # fixed_columns={'headers': True, 'data': 1},
        # valores editaveis
            # editable=True,
        # linha deletavel
        row_deletable=True,
        # opção de download
        export_format='xlsx',
        export_headers='display',
        # paginação
        page_size=20,
        # fixando o header
        fixed_rows={'headers': True},
        # scroll
        style_table={'overflowY': 'auto','overflowx': 'auto'},
        # limitando tamanho da celula
        style_cell={'minWidth': 95, 'maxWidth': 95, 'width': 95, 'textOverflow': 'ellipsis',},
        # mostrar valor da celula
        tooltip_data=[
        {
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
        } for row in df.to_dict('records')
        ],
        tooltip_duration=None,
        # stilizando active cell
        style_data_conditional=[
            {
                'if': {'state': 'active'},
                'backgroundColor': 'blue',
                'color': 'white',
                'border': '0'
            }
        ]
    ),
    html.Button('Add Row', id='editing-rows-button', n_clicks=0),
])

@app.callback(
    Output('adding-rows-table', 'data'),
    Input('editing-rows-button', 'n_clicks'),
    State('adding-rows-table', 'data'),
    State('adding-rows-table', 'columns'))
def add_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows

# @app.callback(
#      Output('adding-rows-table','style_data_conditional'),
#      Input('adding-rows-table','active_cell'),
# )
# def marcando_linha(cell):
#      if cell:
#           return [{'if': {
#                     'row_index': cell['row'],
#                 },
#                 'backgroundColor': 'red',
#                 'color': 'white'}]
#      else:
#           return []

if __name__ == '__main__':
        app.run_server(debug=True,port=8000)
