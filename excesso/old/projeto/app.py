import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP,'https://fonts.googleapis.com/css2?family=Roboto:wght@300;700&display=swap',r'css\Login.css'])

app.layout = html.Div(
    id='login-box',
    className='container',
    children=[
        html.Div(
            id='login-logo',
            children=[
                html.Img(
                    id='login-logo-img',
                    src='assets/logo-semeq-branco.png'
                )
            ]
        ),
        html.Form(
            className='container',
            id='form-box',
            children=[
                html.Div(
                    id='login-title',
                    className='container',
                    children=[
                        html.H1(
                            id='login-title-text',
                            children='Sistema de Gerenciamento do Chatbot'
                        )
                    ]
                ),
                html.Div(
                    id='login-inputs',
                    className='login-inputs',
                    children=[
                        html.Div(
                            className='form-floating mb-3 container',
                            children=[
                                html.Input(
                                    className='form-control',
                                    id='inputEmail',
                                    type='email',
                                    placeholder=''
                                ),
                                html.Label(
                                    htmlFor='inputEmail',
                                    children='Email address'
                                )
                            ]
                        ),
                        html.Div(
                            className='form-floating mb-3 container',
                            children=[
                                html.Input(
                                    className='form-control',
                                    id='inputPassword',
                                    type='password',
                                    placeholder=''
                                ),
                                html.Label(
                                    htmlFor='inputPassword',
                                    children='Password'
                                )
                            ]
                        ),
                        html.A(
                            'Login',
                            className='btn btn-primary',
                            id='btn-login',
                            type='submit'
                        ),
                        html.A(
                            'Forgot Password?',
                            className='small',
                            id='forgot-pass',
                            href='#'
                        )
                    ])
            ])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)