import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

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
                                    dbc.Button("Login", outline=True, color="primary", className="me-1", id='login-button'),
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