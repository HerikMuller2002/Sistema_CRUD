from dash import html

def home_layout():
    # Definindo o layout da página Home
    home = html.Div([
        html.H1('Página Home'),
        html.H3('Bem-vindo!'),
        html.A('Ir para a página de Login', href='/')
    ])
    return home