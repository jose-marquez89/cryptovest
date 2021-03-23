import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

username_group = dbc.FormGroup(
    [
        dbc.Label("Username", html_for="username"),
        dbc.Input(type="email", id="username", placeholder="Enter new username")
    ]
)

password_group = dbc.FormGroup(
    [
        dbc.Label("Password", html_for="password"),
        dbc.Input(type="password", id="password", placeholder="Enter a unique password")
    ]
)

form = dbc.Col(
    dbc.Form([username_group, password_group]), 
    md=4
)

layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Br(), md=12)),
        dbc.Row(
            [
                dbc.Col(md=4), 
                form, 
                dbc.Col(md=4)
            ]
        ),
        dbc.Row()
    ]
)