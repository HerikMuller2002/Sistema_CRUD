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
    layout = html.Div(
            id='login-box',
            className='container',
            children=[
                html.Div(
                    id='login-logo',
                    children=[
                        html.Img(
                            id='login-logo-img',
                            src='assets/img/logo-semeq-branco.png'
                        )
                    ]),
                html.Form(
                    className='container',
                    id='form-box',
                    children=[
                        html.Div(
                            id='login-title',
                            className='container',
                            children=[
                                html.H1(
                                    id='login-title-text',
                                    children='Sistema de gerenciamento de suporte'
                                )
                            ]
                        ),
                        html.Div(
                            id='login-inputs',
                            className='login-inputs',
                            children=[
                                html.Div(
                                    className='form mb-3',
                                    children=[
                                        dcc.Input(
                                            className='form-control',
                                            id='inputEmail',
                                            type='email',
                                            placeholder='Email'
                                        )]
                                ),
                                html.Div(
                                    className='form mb-3',
                                    children=[
                                        dcc.Input(
                                            className='form-control',
                                            id='inputPassword',
                                            type='password',
                                            placeholder='Password'
                                        )]
                                ),
                                html.Div(id="buttons", children=[
                                    html.A(
                                        'Forgot Password?',
                                        # className='btn btn-primary',
                                        id='forgot-pass',
                                        href='#'
                                    ),
                                    html.A(
                                        'Login',
                                        className='btn btn-primary',
                                        id='btn-login',
                                        href='#'
                                    )
                                ])
                            ])
                    ])
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