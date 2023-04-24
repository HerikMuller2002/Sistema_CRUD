import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State
from pages import login, admin, signup

app = dash.Dash(__name__,external_stylesheets=['https://fonts.googleapis.com/css2?family=Roboto:wght@300;700&display=swap'])

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
    
if __name__ == '__main__':
    app.run_server(debug=True,port=5000)