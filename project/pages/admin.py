from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output, State, ALL

import sys
import os

diretorio_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, diretorio_pai)
from database.account import *

df = importar_tabela('project\\database\\banco.db', 'problemas')
df = df.drop(['description','link'], axis=1)
df = df.applymap(lambda x: x.lower().capitalize() if isinstance(x, str) else x)

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
list_subject = []
for subject in list(set(df[df.columns[0]])):
    list_subject.append({"label": subject, "value": 1})

dropdown = html.Div(id='filter', children=[
        dbc.Label(
            html.Span("Subject",
                id="tooltip-target",
                style={"textDecoration": "underline", "cursor": "pointer"}),
                html_for="dropdown"
            ),
            dbc.Tooltip(
                "Assunto do problema",
                target="tooltip-target", placement='top'
            ),
        dcc.Dropdown(id="dropdown-subject",className="mb-3 dpd",
            options=list_subject)
    ])
####################
# table = dbc.Table.from_dataframe(df, striped=False, bordered=False, hover=False, id='table')
table = dbc.Container(class_name='table', children=[
    dash_table.DataTable(
        df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        id='table_id',
        style_header={
            'backgroundColor': '#1c273c',
            'color': 'white',
            'font-weight': 'bold',
            'font-size':'1.7rem',
            'textAlign': 'left',
            'padding': '8px',
            'position': 'sticky',
            'top': '0',
            'z-index': '1',
            'border':'0px',
        },
        style_data={
            'backgroundColor': '#1c273c',
            'color': 'white',
            'textAlign': 'left',
            'border': '5px solid #141c2b'
        },
        style_table={'padding': '0', 'margin': '0', 'height':'100vh'}
    )
])
####################

def admin_style():
    style = '/assets/css/admin.css'
    return style

def admin_layout():
    layout = html.Div([
        html.Header([
            html.Img(src="/assets/img/logo-semeq-branco.png", className="logo"),
        ]),
        html.Div(className="wrapper",children=[
            html.Div(className="sidebar",children=[
                # dropdown
            ]),
            html.Div(className="main",children=[
                dropdown,
                table
            ])
        ])
    ])
    return layout

def callbacks(app):
    @app.callback(Output('tbl_out', 'children'), 
                  Input('tbl', 'active_cell'))
    def update_graphs(active_cell):
        return str(active_cell) if active_cell else "Click the table"
    
    @app.callback(
        Output('output', 'children'),
        [Input({'type': 'dropdown-subject', 'index': ALL}, 'n_clicks')]
    )
    def print_dropdown_value(value):
        for i, n in enumerate(value):
            if n:
                print(f'Opção selecionada: {list_subject[i]["label"]}')