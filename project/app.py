import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State
from pages import login, admin, signup
from database.account import *

# objeto app
app = dash.Dash(__name__,suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP,'https://fonts.googleapis.com/css2?family=Roboto:wght@300;700&display=swap',login.login_style(), signup.signup_style()])


app.config.prevent_initial_callbacks = 'initial_duplicate'

# layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children',allow_duplicate=True),
                [Input('url', 'pathname')],
                prevent_initial_call=True,
                allow_duplicate=True)

def layout_page(pathname):
    if pathname == '/':
        return login.login_layout()
    elif pathname == '/login':
        return login.login_layout()
    elif pathname == '/admin':
        return admin.admin_layout()
    elif pathname == '/register':
        return signup.signup_layout()
    else:
        return '404 Página não encontrada'
    


@app.callback(
    Output('url', 'pathname',allow_duplicate=True),
    Input('login-button', 'n_clicks'),
    Input('signup-button', 'n_clicks'),
    State('username-input', 'value'),
    State('password-input', 'value'),
    prevent_initial_call=True
    )
def update_url(login_clicks, signup_clicks, username, password):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None
    if login_clicks == 0 and signup_clicks == 0:
        button_id = None
    if button_id == "login-button":
        return '/admin'
    elif button_id == "signup-button":
        return '/register'
    else:
        return '/'


@app.callback(Output('password-input', 'value',allow_duplicate=True),
              Output('username-input', 'value',allow_duplicate=True),
              Input('login-button', 'n_clicks'))
def clear_password_field(n_clicks):
    return '',''

#########################################
@app.callback(
    Output('signup-output', 'children',allow_duplicate=True), 
    Input('signup-button', 'value'),
    State('username-input', 'value'),
    State('password-input', 'value'),
    State('confirm-password-input', 'value'),
    prevent_initial_call=True,
    allow_duplicate=True
)
def register(signup_clicks, username, password, confirm_password):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None
    if signup_clicks == 0:
        button_id = None
    if button_id == 'signup-button':
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