from dash import html, dcc
import dash_bootstrap_components as dbc

def signup_style():
    style = '/assets/css/signup.css'
    return style

def signup_layout():
    layout = html.Div(className='main', children=[
        dbc.Row(style={'height': '15vh', 'margin': '0px'}),
        dbc.Row([
            dbc.Col(html.Div()),
            dbc.Col(
                html.Div(className='container', id='signup-box', children=[
                    html.Div(id='logo',children=[
                        html.Img(src='assets/img/logo-semeq-branco.png',alt='logo')
                    ]),
                    html.Form(id='signup-form', className='form', children=[
                        html.Div(id='form-signup', children=[
                            html.H2('Sign Up', className='title'),
                            html.Div(className='form-group', children=[
                                dcc.Input(type='text', id='username-input', placeholder='Username')
                            ]),
                            html.Div(className='form-group', children=[
                                dcc.Input(type='password', id='password-input', placeholder='Password')
                            ]),
                            html.Div(className='form-group', children=[
                                dcc.Input(type='password', id='confirm-password-input', placeholder='Confirm password')
                            ]),
                            html.Div(id='buttons', className='form-group', children=[
                                    dbc.Button("Register", outline=True, color="primary", className="me-1"),
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