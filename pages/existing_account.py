import logging

import flask
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app

FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

user_exists_card = dbc.Col(
    dbc.Card(
        dbc.CardBody([
            html.H4("User Exists"),
            html.P("Sorry, the username you submitted already exists. " 
                   "Please try creating an account with a different username."),
            dcc.Link(
                dbc.Button("Try Again", block=True, color="primary"),
                href="/new-account"
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