import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

import home
import signUp

app = dash.Dash(__name__)

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
    html.Br(),
    html.Div(id='login-output')
])

@app.callback(
    Output('url', 'href'),
    Input('login-button', 'n_clicks'),
    Input('signup-button', 'n_clicks'),
    State('username-input', 'value'),
    State('password-input', 'value')
)
def update_url(login_clicks, signup_clicks, username, password):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id']
    print(button_id)





login_layout = login
home_layout = home.home_layout()
signup_layout = signUp.signUp_layout()

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return login_layout
    elif pathname == '/home':
        return home_layout
    elif pathname == '/signUp':
        return signup_layout
    else:
        return '404 Página não encontrada'

if __name__ == '__main__':
    app.run_server(debug=True)
