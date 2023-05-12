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


######################
search_bar = dbc.Row(id='search',children=[
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
tabelas = listar_tabelas(r'project\database\banco.db')
list_table = []
for tbl in tabelas:
    list_table.append({"label": tbl, "value": tbl})

dropdown_bd = html.Div(id='filter', children=[
        dbc.Label(
            html.Span("Tabela",
                id="tooltip-target"),
                html_for="dropdown"
            ),
            dbc.Tooltip(
                "Assunto do problema",
                target="tooltip-target", placement='top'
            ),
        dcc.Dropdown(id="dropdown_db",className="mb-3 dpd",
            options=list_table,
            value=None)
    ])

####################

def admin_style():
    style = '/assets/css/admin.css'
    return style

def admin_layout():
    layout = html.Div([
        # html.Header([
        #     html.A("Documentation", id="documentation-btn", href='#')
        # ]),
        html.Div(className="wrapper",children=[
            html.Div(className="sidebar",children=[
                html.Img(src="/assets/img/logo-semeq-branco.png", className="logo"),
                dropdown_bd,
            ]),
            html.Div(className="main",children=[
                html.Div(id='filter_table', children=[]),
                dbc.Container(class_name='table',id='table', children=[])
            ])
        ])
    ])
    return layout

def callbacks(app):
    @app.callback(Output('table_out', 'children'), 
                  [Input('table_id', 'active_cell'),Input('table_id', 'data')])
    def update_graphs(active_cell, df):
        if active_cell:
            ...
        return str(active_cell)
    
    @app.callback([Output('filter_table', 'children'), Output('table', 'children')],
                  Input('dropdown_db', 'value'))
    def choice_table(value):
        if value is not None:
            df = importar_tabela('project\\database\\banco.db', value)
            try:
                df = df.drop(['description','link'], axis=1)
            except KeyError:
                df = df.drop(['id'], axis=1)
            except KeyError:
                pass
            df.astype(str)
            df = df.applymap(lambda x: x.lower().capitalize() if isinstance(x, str) else x)

            lista = df.to_dict('records')

            list_subject = []
            for subject in list(set(df[df.columns[0]])):
                list_subject.append({"label": subject, "value": subject})

                dropdown = [html.Div(id='buttons_crud', children=[
                            dbc.Button(html.Img(src=r"assets\img\plus-solid.svg"), color="success", className="me-1", id='edit'),
                            dbc.Button(html.Img(src=r"assets\img\pen-to-square-solid.svg"), color="primary", className="me-1", id='edit'),
                            dbc.Button(html.Img(src=r"assets\img\trash-can-solid.svg"), color="danger", className="me-1", id='edit'),
                            ]),
                            html.Div(id='right-header',children=[
                                html.A(['Documentation']),
                                dcc.Dropdown(id="my-dropdown",className="mb-3 dpd",
                                options=list_subject,value=None),
                                dbc.Button("Export", color="secondary", className="me-1"),
                            ])]
            
            table = dash_table.DataTable(
                        df.to_dict('records'),
                        columns=[{"name": i, "id": i} for i in df.columns],
                        id='table_id',
                        style_header={
                            'backgroundColor': '#1c273c',
                            'color': 'white',
                            'font-weight': 'bold',
                            'font-size':'1.2rem',
                            'textAlign': 'left',
                            'padding': '8px',
                            'position': 'sticky',
                            'top': '0',
                            'z-index': '1',
                            'border':'0px',
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
                            'overflowY': 'scroll',
                            'overflowX': 'scroll',
                            }
                    )

            with open(r'project\log\table_log.json','w', encoding='utf-8') as db:
                json.dump(lista, db)

            return dropdown, table
        else:
            with open(r'project\log\table_log.json','w', encoding='utf-8') as db:
                json.dump([], db)
            p = html.P("No table", style={'color':'white'})
            return '', p
    
    @app.callback(Output("table_id", "data"), 
                  [State('table_id', "data"), Input("my-dropdown", "value")])
    def update_output(data,value):
        with open(r'project\log\table_log.json','r', encoding='utf-8') as db:
                db = db.read()
                df = json.loads(db)
        if value is not None:
            try:
                df1 = pd.DataFrame(df)
                df2 = df1.loc[df1.iloc[:, 0] == value]
                return df2.to_dict('records')
            except:
                return df
        else:
            return df