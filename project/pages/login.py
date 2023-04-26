import sys
import os
import dash
import dash_bootstrap_components as dbc
from flask import session
from dash import html, dcc
from dash.dependencies import Input, Output, State

diretorio_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, diretorio_pai)
from database.account import *

def login_style():
    style = '/assets/css/login.css'
    return style

def login_layout():
    layout = html.Div(style={'height':'100vh'},children=[
        dbc.Row(style={'height': '17vh', 'margin': '0px'}, children=[
            dbc.Col(),
            dbc.Col(dbc.Modal(id="modal-sm",size='sm', is_open=False, children=[
                dbc.ModalHeader(dbc.ModalTitle("Authentication Error")),
                dbc.ModalBody("Invalid username or password!"),
                dbc.ModalFooter(style={'font-size':'15px','font-weight':'bold'},children=[html.A('Please try again',id='try-again')])
                ])),
            dbc.Col()
        ]),
        dbc.Row(style={'height': '60vh', 'margin': '0px'}, children=[
            dbc.Col(),
            dbc.Col(
                html.Div(className='container', id='login-box', children=[
                    html.Div(id='logo',children=[
                        html.Img(src='assets/img/logo-semeq-branco.png',alt='logo')
                    ]),
                    html.Form(id='login-form', className='form', children=[
                        html.Div(id='form-login', children=[
                            html.H2('Login', className='title'),
                            html.Div(className='form-group', children=[
                                dcc.Input(type='text', id='username-input', placeholder='Username')
                            ]),
                            html.Div(className='form-group', children=[
                                dcc.Input(type='password', id='password-input', placeholder='Password')
                            ]),
                            html.Div(id='buttons', className='form-group', children=[
                                    dbc.Button("Login", type='button', color="primary",outline=True, className="me-1", id='login-button', n_clicks=0),
                                    html.A('Register here', href='/register', id='signup-button')
                            ])
                        ])
                    ])
                ])
            ),
            dbc.Col()
        ]),
        dbc.Row(style={'height': '23vh', 'margin': '0px'}, children=[])
    ])

    return layout

def callbacks(app):
    @app.callback(
        Output("modal-sm", "is_open"),
        [Input('login-button','n_clicks')],
        [Input('try-again','n_clicks')],
        [State('username-input','value'), State('password-input','value')],
        [State("modal-sm", "is_open")]
    )
    def message_error(button,try_again,username,password,is_open):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None
        if button_id == "login-button":
            verify = verify_acces(username,password)
            if verify:
                return is_open
            else:
                return not is_open
            
    @app.callback(Output('password-input', 'value'),
              Output('username-input', 'value'),
              Input('login-button', 'n_clicks'))
    def clear_fields(n_clicks):
        return '',''

    @app.callback(
        Output('url', 'pathname'),
        Input('login-button','n_clicks'),
        [State('username-input','value'), State('password-input','value')]
    )
    def update_url(button,username,password):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None
        if button_id == "login-button":
            verify = verify_acces(username,password)
            if verify:
                session['user'] = username
                return '/admin'
        return dash.no_update