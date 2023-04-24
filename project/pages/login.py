import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from flask import Flask, session
from database.account import *

def login_style():
    style = '/assets/css/login.css'
    return style

def login_layout():
    layout = html.Div(className='main', children=[
        dbc.Row(style={'height': '15vh', 'margin': '0px'}),
        dbc.Row([
            dbc.Col(html.Div()),
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
                                    dbc.Button("Login", color="primary",outline=True, className="me-1", id='login-button', n_clicks=0),
                                    html.A('Register here', href='/register', id='signup-button')
                            ])
                        ])
                    ])
                ])
            ),
            dbc.Col(html.Div())
        ]),
        dbc.Row(style={'height': '15vh', 'margin': '0px'})
    ])

    return layout

def callbacks(app):
    @app.callback(Output('url', 'pathname'),
                Input('login-button', 'n_clicks'),
                Input('signup-button', 'n_clicks'),
                State('username-input', 'value'),
                State('password-input', 'value'),
                prevent_initial_call=True,
                allow_duplicate=True)
    def update_url(login_clicks, signup_clicks, username, password):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None
        if login_clicks == 0 and signup_clicks == 0:
            button_id = None
        if button_id == "login-button":
            verify = verify_acces(username, password)
            if not verify:
                return '/'
            else:
                session['user'] = username
                return '/admin'
        elif button_id == "signup-button":
            return '/register'
        else:
            return '/'


    @app.callback(Output('password-input', 'value',allow_duplicate=True),
                Output('username-input', 'value',allow_duplicate=True),
                Input('login-button', 'n_clicks'),
                prevent_initial_call=True)
    def clear_password_field(n_clicks):
        return '',''