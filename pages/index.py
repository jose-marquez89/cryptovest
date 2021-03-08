import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

details = dbc.Col(
    [
        html.H3("Keep Track Of Your Crypto Investments"),
        html.P("Create an account and start tracking your crypto transactions free of charge."),
        dcc.Link(
            dbc.Button('Create Account', color='primary'),
            href='#'
        )
    ],
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