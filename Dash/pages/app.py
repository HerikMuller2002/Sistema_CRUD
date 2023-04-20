import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# Cria a instância do objeto Dash
app = dash.Dash(__name__, external_stylesheets=['style.css', dbc.themes.BOOTSTRAP])

# Define o layout do navbar
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src='http://placehold.it/200x50&text=LOGO', height="30px")),
                    ],
                    align="center",
                ),
                href="#",
            ),
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("Stats", href="#", active=True)),
                    dbc.DropdownMenu(
                        [
                            dbc.DropdownMenuItem("Edit Profile", href="#"),
                            dbc.DropdownMenuItem("Change Password", href="#"),
                            dbc.DropdownMenuItem(divider=True),
                            dbc.DropdownMenuItem("Logout", href="#"),
                        ],
                        nav=True,
                        in_navbar=True,
                        label="Admin User",
                    ),
                ],
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
)

# Define o layout da sidebar
sidebar = dbc.Nav([
        html.H2("MENU"),
        html.Hr(),
        dbc.NavItem(dbc.NavLink("MENU 1", href="#")),
        dbc.Collapse(
            [
                dbc.NavItem(dbc.NavLink("SUBMENU 1.1", href="#")),
                dbc.NavItem(dbc.NavLink("SUBMENU 1.2", href="#")),
                dbc.NavItem(dbc.NavLink("SUBMENU 1.3", href="#")),
            ],
            id="submenu-1-items",
        ),
        dbc.NavItem(dbc.NavLink("MENU 2", href="#")),
        dbc.Collapse(
            [
                dbc.NavItem(dbc.NavLink("SUBMENU 2.1", href="#")),
                dbc.NavItem(dbc.NavLink("SUBMENU 2.2", href="#")),
                dbc.NavItem(dbc.NavLink("SUBMENU 2.3", href="#")),
            ],
            id="submenu-2-items",
        ),
        dbc.NavItem(dbc.NavLink("MENU 3", href="#")),
        dbc.NavItem(dbc.NavLink("MENU 4", href="#")),
        dbc.NavItem(dbc.NavLink("MENU 5", href="#")),
    ],
    vertical=True,
    pills=True,
)

# Define o layout completo
app.layout = dbc.Container(
    [
        # Adiciona o navbar e a sidebar ao container
        navbar,
        dbc.Row(
            [
                dbc.Col(
                    sidebar,
                    width={"size": 3},
                    style={"border-right": "1px solid lightgray", "padding-right": "30px"},
                ),
                dbc.Col(html.Div("Conteúdo da página")),
            ],
            align="start",
        ),
    ],
    fluid=True,
)

# Inicia o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
