from dash import html, dcc
from dash.dependencies import Input

def signUp_layout():
    signUp = html.Div([
        html.H1('Sign Up'),
        html.A('Voltar para a página de Login', href='/'),
        dcc.Input(
            id='username-submmit',
            type='text',
            placeholder='nome de usuário'
        ),
        dcc.Input(
            id='password-submmit',
            type='password',
            placeholder='senha'
        ),
        dcc.Input(
            id='confirm-password',
            type='password',
            placeholder='confirme a senha'
        ),
        html.Button('Sign Up', id='signup_submmit', n_clicks=0),
        html.Br(),
        html.Div(id='signup-output'), # Novo elemento Div
    ])

    return signUp