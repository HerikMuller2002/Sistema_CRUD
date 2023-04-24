from dash import html,dash_table
import dash_bootstrap_components as dbc
import pandas as pd

import sys
import os
# Adicionar a pasta pai ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Agora você pode importar do pacote database
from database.account import *

df = importar_tabela('project\\database\\banco.db', 'problemas')

def admin_layout():
    layout = html.Div([
        html.Div([
            dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
        ])
    ])
    return layout