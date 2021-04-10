import logging

import flask
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
from db_users import create_new_user, validate_user
from db_model import load_engine

FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

username_group = dbc.FormGroup(
    [
        dbc.Input(name="username", placeholder="Enter username")
    ],
)

password_group = dbc.FormGroup(
    [
        dbc.Input(type="password", name="password", placeholder="Enter password")
    ]
)

form = dbc.Col(
    dbc.Card(
        dbc.CardBody([
            # for some reason, this does NOT work with dbc.Form
            # will not hit the /submit route
            html.H4("Login"),
            html.Br(),
            html.Form(
                [
                    username_group,
                    password_group,
                    dbc.Button("Submit", id="submit-button", block=True, color="primary")
                ],
                id="login-uname-pw-submit",
                action="/login-submit",
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

@app.server.route("/login-submit", methods=["POST"])
def submit_login():
    logging.debug("submit triggered")
    details = flask.request.form
    logging.debug(details)
    username = details.get("username")
    password = details.get("password")
    
    engine = load_engine()
    validation = validate_user(username, password)
    if validation == 0:
        res = flask.redirect('/login-success')
        res.set_cookie('logged-in-user', username)
        return res
    elif validation == 1:
        return flask.jsonify({"pw": "fail"})
    else:
        return flask.jsonify({"user": "does not exist"})

@app.server.route('/login-success')
def greet_user():
    user = flask.request.cookies.get('logged-in-user')
    return f"<H1>Hello {user}!</H1><p>Return to main page to continue</p>"