import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from database.account import *

def signup_style():
    style = '/assets/css/signup.css'
    return style

def signup_layout():
    layout = html.Div(className='main', children=[
        dbc.Row(style={'height': '15vh', 'margin': '0px'}),
        dbc.Row([
            dbc.Col(html.Div()),
            dbc.Col(
                html.Div(className='container', id='signup-box', children=[
                    html.Div(id='logo',children=[
                        html.Img(src='assets/img/logo-semeq-branco.png',alt='logo')
                    ]),
                    html.Form(id='signup-form', className='form', children=[
                        html.Div(id='form-signup', children=[
                            html.H2('Sign Up', className='title'),
                            html.Div(className='form-group', children=[
                                dcc.Input(type='text', id='username-input', placeholder='Username')
                            ]),
                            html.Div(className='form-group', children=[
                                dcc.Input(type='password', id='password-input', placeholder='Password')
                            ]),
                            html.Div(className='form-group', children=[
                                dcc.Input(type='password', id='confirm-password-input', placeholder='Confirm password')
                            ]),
                            html.Div(id='buttons', className='form-group', children=[
                                    dbc.Button("Register", outline=True, color="primary", className="me-1", id='signup-submit'),
                                    html.A('Return to login', href='/login', id='login')
                            ]),
                            html.Div(id='signup-output'), # Novo elemento Div
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
    @app.callback(
        Output('signup-output', 'children',allow_duplicate=True), 
        Input('signup-submit', 'n_clicks'),
        State('username-input', 'value'),
        State('password-input', 'value'),
        State('confirm-password-input', 'value'),
        prevent_initial_call=True
    )
    def register(signup_clicks, username, password, confirm_password):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None
        if signup_clicks == 0:
            button_id = None
        if button_id == 'signup-submit':
            if len(password) == 0 or password == None and confirm_password == None or len(password) == 0 and len(confirm_password) == 0:
                return 'Cadastre uma senha'
            elif len(password) < 8 or len(confirm_password) < 8:
                return 'A senha deve ter no mínimo 8 caracteres'
            elif password != confirm_password:
                return 'As senhas não coincidem. Tente novamente.'
            else:
                create_acces(username, password)
                return 'Cadastro realizado com sucesso! Faça login para acessar a página inicial.'