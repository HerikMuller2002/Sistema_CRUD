from dash import html, dcc
from dash.dependencies import Input

def signUp_layout():
    signUp = html.Div([
        html.H1('Sign Up'),
        dcc.Input(
            id='username-input',
            type='text',
            placeholder='nome de usuário'
        ),
        dcc.Input(
            id='password-input',
            type='password',
            placeholder='senha'
        ),
        dcc.Input(
            id='password-input',
            type='password',
            placeholder='confirme a senha'
        ),
        html.Button('Sign Up', id='login-button', n_clicks=0),
    ])

    return signUp