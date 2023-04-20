import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State
from pages import login, home, signUp
from database.account import *
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

modal_layout = html.Div([
    html.H1('Olá')
])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
                [Input('url', 'pathname')],
                prevent_initial_call=True,
                allow_duplicate=True)

def display_page(pathname):
    if pathname == '/':
        return login.login_layout()
    elif pathname == '/login':
        return login.login_layout()
    elif pathname == '/home':
        return home.home_layout()
    elif pathname == '/signUp':
        return signUp.signUp_layout()
    else:
        return '404 Página não encontrada'



#########################################
login_layout = login.login_layout()

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
            return '/home'
    elif button_id == "signup-button":
        return '/signUp'
    else:
        return '/'

@app.callback(Output('password-input', 'value'),
              Output('username-input', 'value'),
              Input('login-button', 'n_clicks'))
def clear_password_field(n_clicks):
    return '',''

@app.callback(
    Output('papagaio','children'),
    Input('modal-button','n_clicks'),
    prevent_initial_call=True
)
def modal(click):
    if click is None:
        raise PreventUpdate
    return modal_layout


#########################################
signUp_layout = signUp.signUp_layout()

@app.callback(
    Output('signup-output', 'children'), 
    Input('signup_submmit', 'n_clicks'),
    State('username-submmit', 'value'),
    State('password-submmit', 'value'),
    State('confirm-password', 'value'),
    prevent_initial_call=True,
    allow_duplicate=True
)
def register(signup_clicks, username, password, confirm_password):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None
    if signup_clicks == 0:
        button_id = None
    if button_id == 'signup_submmit':
        if len(password) == 0 or password == None and confirm_password == None or len(password) == 0 and len(confirm_password) == 0:
            return 'Cadastre uma senha'
        elif len(password) < 8 or len(confirm_password) < 8:
            return 'A senha deve ter no mínimo 8 caracteres'
        elif password != confirm_password:
            return 'As senhas não coincidem. Tente novamente.'
        else:
            create_acces(username, password)
            return 'Cadastro realizado com sucesso! Faça login para acessar a página inicial.'

if __name__ == '__main__':
    app.run_server(debug=True,port=5000)
