from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

import sys
import os

diretorio_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, diretorio_pai)
from database.account import *

df = importar_tabela('project\\database\\banco.db', 'problemas')

######################
search_bar = dbc.Row(id='search',children=[
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary",outline=True, className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)
######################
dropdown = html.Div(id='filter',children=[
        dbc.Label("Subject", html_for="dropdown"),
        dcc.Dropdown(
            id="dropdown-subject",
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Option 3", "value": 3},
                {"label": "Option 4", "value": 4},
                {"label": "Option 5", "value": 5},
            ],
        ),
        dbc.Label("Device", html_for="dropdown"),
        dcc.Dropdown(
            id="dropdown-device",
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Option 3", "value": 3},
                {"label": "Option 4", "value": 4},
                {"label": "Option 5", "value": 5},
            ],
        ),
        dbc.Label("Interface", html_for="dropdown"),
        dcc.Dropdown(
            id="dropdown-interface",
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Option 3", "value": 3},
                {"label": "Option 4", "value": 4},
                {"label": "Option 5", "value": 5},
            ],
        ),
        dbc.Label("Model", html_for="dropdown"),
        dcc.Dropdown(
            id="dropdown-model",
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Option 3", "value": 3},
                {"label": "Option 4", "value": 4},
                {"label": "Option 5", "value": 5},
            ],
        ),
    ],
    className="mb-3",
)
####################
table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
####################

def admin_style():
    style = '/assets/css/admin.css'
    return style

def admin_layout():
    layout = html.Div([
        html.Header([
            html.Img(src="/assets/img/logo-semeq-branco.png"),
        ]),
        html.Div(className="wrapper",children=[
            html.Div(className="sidebar",children=[
                dropdown
            ]),
            html.Div(className="main",children=[
                html.H1("Administração"),
                table
            ])
        ])
    ])
    return layout