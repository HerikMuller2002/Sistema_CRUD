from flask_session import Session
from flask import Flask, session

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State
from pages import login, admin, signup

# objeto app
app = dash.Dash(__name__,suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP,'https://fonts.googleapis.com/css2?family=Roboto:wght@300;700&display=swap',login.login_style(), signup.signup_style()])
app.config.prevent_initial_callbacks = 'initial_duplicate'

# objeto server
server = Flask(__name__)
app.server.secret_key = 'fasfasf'
server.config['SESSION_TYPE'] = 'filesystem'
Session(server)

# layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', style={'height':'100vh', 'width':'100vw'})
])

@app.callback(Output('page-content', 'children',allow_duplicate=True),
                [Input('url', 'pathname')],
                prevent_initial_call=True,
                allow_duplicate=True)
def layout_page(pathname):
    if pathname == '/' or pathname == '/login':
        session.clear()
        return login.login_layout()
    elif pathname == '/admin' and 'user' in session:
            return admin.admin_layout()
    elif pathname == '/register':
        return signup.signup_layout()
    else:
        return '404 Página não encontrada'
    
login.callbacks(app)
signup.callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True,port=5000)