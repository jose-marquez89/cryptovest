import logging

import flask
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from db_users import get_user_id

FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)


user_exists_card = dbc.Col(
    dbc.Card(
        dbc.CardBody([
            html.H4(id='logged-in-user-greeting'),
            html.P(id='action-call'),
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

@app.callback([
    Output('logged-in-user-greeting', 'children'),
    Output('action-call', 'children')
], [Input('action-call', 'children')])
def get_user(_):
    user = flask.request.cookies.get('logged-in-user')
    id_ = get_user_id(user)
    message = f"Your user id is {id_}"

    if not id_:
        user = "stranger"
        message = "Log in to start tracking"
    return f"Hello {user}!", message 