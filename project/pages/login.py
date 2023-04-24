import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from flask import Flask, request

app = dash.Dash(__name__,external_stylesheets=['/assets/login.css',dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div(className='main', children=[
    dbc.Row(style={'height': '20vh', 'margin': '0px'}),
    dbc.Row([
        dbc.Col(html.Div()),
        dbc.Col(
            html.Div(className='container', id='login-box', children=[
                html.Div(id='logo',children=[
                    html.Img(src='assets/logo-semeq-branco.png',alt='logo')
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
                                dbc.Button("Login", outline=True, color="primary", className="me-1"),
                                html.A('Register here', href='#', id='register')
                        ])
                    ])
                ])
            ])
        ),
        dbc.Col(html.Div())
    ]),
    dbc.Row(style={'height': '20vh', 'margin': '0px'})
])


k = Flask(__name__)

CSS_FILES = {
    'home': 'styles/home.css',
    'about': 'styles/about.css',
    'contact': 'styles/contact.css'
}

def get_css():
    page_name = request.path[1:]
    css_file = f"styles/{page_name}.css"
    return css_file

@k.route('/')
def index():
    css_file = get_css()
    return css_file

a = index()
print(a)


if __name__ == '__main__':
    app.run_server(debug=True)