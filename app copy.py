import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Store(id='ctrl-key-store'),
    html.Div(id='output'),
    html.Button('Click me', id='button')
])


@app.callback(
    Output('ctrl-key-store', 'data'),
    Input('button', 'n_clicks'),
    State('ctrl-key-store', 'data'),
    prevent_initial_call=True
)
def update_ctrl_key_status(n_clicks, ctrl_key_status):
    ctx = dash.callback_context
    if ctx.triggered[0]['prop_id'] == 'button.n_clicks':
        key_status = ctx.states['ctrl-key-store.data'] or {}
        key_status[n_clicks] = True
        return key_status
    else:
        return ctrl_key_status


@app.callback(
    Output('output', 'children'),
    Input('ctrl-key-store', 'modified_timestamp'),
    State('ctrl-key-store', 'data'),
    prevent_initial_call=True
)
def handle_click(modified_timestamp, ctrl_key_status):
    ctx = dash.callback_context
    if ctx.triggered[0]['prop_id'] == 'ctrl-key-store.modified_timestamp':
        last_key_status = ctx.states['ctrl-key-store.data']
        last_n_clicks = max(last_key_status.keys())
        if last_key_status[last_n_clicks]:
            return 'Mouse click with Ctrl key pressed'
        else:
            return 'Mouse click without Ctrl key'
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True,port=5000)
