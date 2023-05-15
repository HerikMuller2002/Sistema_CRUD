from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output, State, ALL

import sys
import os
import json
from datetime import datetime

diretorio_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, diretorio_pai)
from database.account import *

####################
list_bd = ['bd1','bd2']
dropdown_bd = html.Div(id='filter', children=[
        dbc.Label("database"),
        dcc.Dropdown(id="dropdown_db",className="mb-3 dpd",
            options=list_bd,
            value=None)
    ])

tabelas = listar_tabelas(r'project\database\banco.db')
list_table = []
for tbl in tabelas:
    list_table.append({"label": tbl, "value": tbl})

dropdown_table = html.Div(id='filter', children=[
        dbc.Label("Table"),
        dcc.Dropdown(id="dropdown_table",className="mb-3 dpd",
            options=list_table,
            value=None)
    ])
####################
search_bar = dbc.Row(id='search-bar',children=[
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary",outline=False, className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)
####################
df = importar_tabela('project\\database\\banco.db', 'problemas')
try:
    df = df.drop(['description','link'], axis=1)
except KeyError:
    pass
df.astype(str)
df = df.applymap(lambda x: x.lower().capitalize() if isinstance(x, str) else x)
table = dash_table.DataTable(
            df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in df.columns],
            id='table_id',
            style_cell={'minWidth': 95, 'maxWidth': 95, 'width': 95, 'textOverflow': 'ellipsis',},
            tooltip_data=[
                {
                    column: {'value': str(value), 'type': 'markdown'}
                    for column, value in row.items()
                } for row in df.to_dict('records')
                ],
                tooltip_duration=None,
            style_header={
                'backgroundColor': '#1c273c',
                'color': 'white',
                'font-weight': 'bold',
                'font-size':'1.2rem',
                'textAlign': 'left',
                'padding': '8px',
                'top': '0',
                'z-index': '1',
                'border': '2px solid #141c2b',
                'border-top': '0',
                'position':'sticky'
            },
            style_data={
                'backgroundColor': '#293751',
                'color': 'white',
                'textAlign': 'left',
                'border': '2px solid #141c2b',
                'padding': '8px',
                'font-size':'1rem'
            },
            style_table={
                'padding': '0', 
                'margin': '0', 
                'height':'85vh',
                'width':'83vw',
                'overflowY': 'auto',
                'overflowx': 'auto',
                'font-family': 'Roboto'
                },
            style_data_conditional=[{}]
        )

####################
def admin_style():
    style = '/assets/css/admin.css'
    return style

####################
def admin_layout():
    layout = html.Div([
        html.Div(id="wraper",children=[
            html.Div(id="sidebar",children=[
                html.Div(id="sidebar-logo",children=[
                    html.Img(src="/assets/img/logo-semeq-branco.png", id="logo"),
                ]),
                html.Div(id="sidebar-filter",children=[
                    dropdown_bd,
                    dropdown_table,
                ])
            ]),
            html.Div(id="main-content",children=[
                html.Div(id='table-actions',children=[
                    html.Div(id='crud',children=[
                        dbc.Button(color="success", className="me-1", id='add-row',children=[
                            html.P('Add row'),
                            html.Img(src=r"assets\img\plus-solid.svg")
                            ]),
                        dbc.Button(color="primary", className="me-1", id='btn-crud',children=[
                            html.P('Edit'),
                            html.Img(src=r"assets\img\pen-to-square-solid.svg")
                            ]),
                        dbc.Button(color="danger", id='btn-crud',children=[
                            html.P('Delete'),
                            html.Img(src=r"assets\img\trash-can-solid.svg")
                            ]),
                    ]),
                    html.Div(id='search',children=[
                        search_bar
                    ]),
                    html.Div(id='help-export',children=[
                        dbc.Button(color="secondary", className="me-1",id='btn-help',children=[
                            html.P('Help'),
                            html.Img(src=r"\assets\img\circle-question-regular.svg")
                        ]),
                        dbc.Button(color="primary", className="me-1",id='btn-export',disabled=True,children=[
                            html.P('Download'),
                            html.Img(src=r"\assets\img\file-export-solid.svg")
                        ])
                    ]),
                ]),
                html.Div(id='table',children=[
                    table
                ]),
            ])
        ])
    ])
    return layout

####################
selected_cell = None
def callbacks(app):
    # @app.callback(
    #     [Output('table_id','style_data_conditional')],
    #     [Input('table_id','active_cell')],
    # )

    @app.callback(
     Output('table_id','style_data_conditional'),
     Input('table_id','active_cell'),
    )
    def marcando_linha(cell):
        global selected_cell
        if cell:
            return [{'if': {
                        'row_index': cell['row'],
                    },
                    'backgroundColor': 'rgb(1, 104, 250, 0.6)',
                    'color': 'white',
                    'border': '0',
                    'border-left': '0',
                    'border-right': '0'
                    },
                    {
                    'if': {'state': 'active'},
                    'backgroundColor': 'rgb(1, 104, 250, 0.6)',
                    'color': 'white',
                    'border': '0',
                    'border-left': '0',
                    'border-right': '0'
                    # 'border': '0'
                    }]
        else:
            return []