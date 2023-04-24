import dash
from dash.dependencies import Input, Output, State
from app import app

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
        verify = True #verify_acces(username, password)
        if not verify:
            return '/'
        else:
            return '/admin'
    elif button_id == "register":
        return '/signup'
    else:
        return '/'

@app.callback(Output('password-input', 'value'),
              Output('username-input', 'value'),
              Input('login-button', 'n_clicks'))
def clear_password_field(n_clicks):
    return '',''

callbacks = {
    'update_url': update_url(None,None,None,None),
    'clear_password_field': clear_password_field(None)
}