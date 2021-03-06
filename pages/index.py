import flask
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from db_users import get_user_id

details = dbc.Col(
    id='index-action-call',
    md=4
)

photo = dbc.Col(
    [
        html.Img(src='assets/nick-chong-charts.jpg',
                 className='img-fluid'),
        html.P(
            children=[
                "Photo Credit: ",
                html.A("Nick Chong", href="https://twitter.com/n1ckchong?utm_medium=referral&utm_source=unsplash")
            ]
        )
    ],
    md=8
)

layout = dbc.Row([details, photo])

@app.callback(Output('index-action-call', 'children'),
              Input('index-action-call', 'children'))
def set_link(_):
    user = flask.request.cookies.get('logged-in-user')

    if user:
        action = [
            html.H3("Keep Track Of Your Crypto Investments"),
            html.P("Update your ledger to get your latest portfolio analysis."),
            dcc.Link(dbc.Button('Get Started', color='primary'), href="#")
        ]
    else:
        action = [
            html.H3("Keep Track Of Your Crypto Investments"),
            html.P("Create an account and start tracking your crypto transactions free of charge."),
            dcc.Link(dbc.Button('Create Account', color='primary'), href="/new-account")
        ]
    
    return action 
