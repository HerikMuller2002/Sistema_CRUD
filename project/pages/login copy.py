import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,external_stylesheets=['/assets/css/login.css',dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div(className='main', children=[
    dbc.Row(style={'height': '20vh', 'margin': '0px'}),
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


if __name__ == '__main__':
    app.run_server(debug=True)