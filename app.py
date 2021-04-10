import dash
import dash_bootstrap_components as dbc

external_stylesheets = [
    dbc.themes.DARKLY,
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css'
]

meta_tags = [
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                meta_tags=meta_tags, suppress_callback_exceptions=True)

if __name__ == "__main__":
    app.run_server(debug=True)