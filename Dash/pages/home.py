from dash import html,dash_table
import dash_bootstrap_components as dbc
import pandas as pd

import sys
import os
# Adicionar a pasta pai ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Agora você pode importar do pacote database
from database.account import *

df = importar_tabela('Dash\\database\\banco.db', 'problemas')

def home_layout():
    table = dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        style_table={'height': '500px','width': '70%', 'overflowY': 'auto', 'overflowX': 'auto'},
        style_cell={'minWidth': '0px', 'maxWidth': '780px', 'minHeight': '0px', 'maxHeight': '180px', 'whiteSpace': 'normal', 'text-allingn': 'left'},
        style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'}
    )

    home = html.Div([
        html.Div([
        html.Nav
        ])
    ])
    return home
