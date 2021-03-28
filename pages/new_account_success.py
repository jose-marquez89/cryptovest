import logging

import flask
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from app import app

FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

user_exists_card = dbc.Col(
    dbc.Card(
        dbc.CardBody([
            html.H4("Success!"),
            html.P("You've created a new account. Log in to start tracking."),
            dcc.Link(
                dbc.Button("Log In", block=True, color="primary"),
                href="#"
            )
        ])
    ), 
    md=4
)

layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Br(), md=12)),
        dbc.Row(
            [
                dbc.Col(md=4), 
                user_exists_card, 
                dbc.Col(md=4)
            ]
        ),
        dbc.Row()
    ]
)