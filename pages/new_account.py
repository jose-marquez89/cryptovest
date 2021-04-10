import logging

import flask
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
from db_users import create_new_user
from db_model import load_engine

FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

username_group = dbc.FormGroup(
    [
        dbc.Input(name="username", placeholder="Enter new username")
    ],
)

password_group = dbc.FormGroup(
    [
        dbc.Input(type="password", name="password", placeholder="Enter a unique password")
    ]
)

form = dbc.Col(
    dbc.Card(
        dbc.CardBody([
            # for some reason, this does NOT work with dbc.Form
            # will not hit the /submit route
            html.H4("New Account"),
            html.Br(),
            html.Form(
                [
                    username_group,
                    password_group,
                    dbc.Button("Submit", id="submit-button", block=True, color="primary")
                ],
                id="uname-pw-submit",
                action="/submit",
                method="post"
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
                form, 
                dbc.Col(html.Div(id="submit-message"), md=4)
            ]
        ),
        dbc.Row()
    ]
)

@app.server.route("/submit", methods=["POST"])
def submit_new_acc():
    logging.debug("submit triggered")
    details = flask.request.form
    logging.debug(details)
    username = details.get("username")
    password = details.get("password")
    
    if create_new_user(username, password) == 1:
        return flask.redirect("/existing-account")

    return flask.redirect("/new-account-success") 