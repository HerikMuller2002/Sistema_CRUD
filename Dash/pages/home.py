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
        df.to_dict('records'), [{"name": i, "id": i} for i in df.columns]
        )

    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href='/home')),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("Login", href='/'),
                    dbc.DropdownMenuItem("Sign up", href="/signUp"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="NavbarSimple",
        brand_href="#",
        color="primary",
        dark=True,
        )

    # Definindo o layout da página Home
    home = html.Div([
        navbar,
        html.H1('Página Home'),
        table
    ])
    return home