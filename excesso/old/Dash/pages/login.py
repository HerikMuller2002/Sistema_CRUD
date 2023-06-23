import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

def login_layout():
    login = html.Div([
        html.H1('Página de Login'),
        dcc.Input(
            id='username-input',
            type='text',
            placeholder='Insira seu nome de usuário',
        ),
        dcc.Input(
            id='password-input',
            type='password',
            placeholder='Insira sua senha'
        ),
        html.Button('Login', id='login-button', n_clicks=0),
        html.Button('Sign up', id='signup-button', n_clicks=0),
        html.Button('modal', id='modal-button', n_clicks=0),
        html.Br(),
        html.Div(id='login-output'),
        html.Div(id='denied'),
        html.Div(
            id='papagaio',
            className='pirata',
            children=[
                
            ]
        ),

    ])

    return login