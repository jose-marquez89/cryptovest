import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from pages import index, login

external_stylesheets = [
    dbc.themes.DARKLY,
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css'
]

meta_tags = [
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                meta_tags=meta_tags)

navbar = dbc.NavbarSimple(
    brand='Crypto Investment Tracker',
    brand_href='/',
    children=[
        dbc.NavItem(dcc.Link('Log In', href='#', className='nav-link')),
        dbc.NavItem(dcc.Link('Sign Up', href='#', className='nav-link'))
    ],
    sticky='top',
    color='primary',
    dark=True
)

footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P([
                html.Span('Jose Marquez', className='mr-2'),
                html.A(
                    html.I(className='fab fa-github-square mr-1'),
                    href='https://github.com/jose-marquez89'
                )
            ],
            className='lead')
        )
    )
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(id='page-content', className='mt-4'),
    html.Hr(),
    footer
])

app.title = "Crypto Investment Tracker"

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/login':
        return login.layout
    else:
        return html.H2("Page Not Found")