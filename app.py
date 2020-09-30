import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import indexString
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],suppress_callback_exceptions=True)
server = app.server
app.title = 'CdP ESFM'
app.index_string = indexString.string
logo = "http://www.unamglobal.unam.mx/wp-content/uploads/2017/05/LOGO-UNAM.png"
color_fondo = '#ffffff' #'rgb(5,27,83)'#'061d47'

app.layout = html.Div([
                    dcc.Store(id='memory_test404'),
                    dcc.Store(id='memory_test'),
                    dcc.Store(id='session-stored2', data=[],storage_type='session'),
                    dcc.Location(id='url', refresh=False),
                    dbc.Navbar([html.A( dbc.Row(
                                            [
                                                dbc.Col(html.Img(src=logo, height="30px")),
                                                dbc.Col(dbc.NavbarBrand("FES Acatlán | MAC - 1152", className="ml-2")),
                                            ],
                                            align="center",
                                            no_gutters=True,
                                        ),
                                        href="/",
                                    ),
                                    dbc.NavbarToggler(id="navbar-toggler"),
                                    #dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
                                ],
                                color="dark",
                                dark=True,
                                sticky = 'top'
                            ),
                    html.Div(id = 'principal-screen',style = {'background-color':color_fondo})
                    ])

@app.callback([Output('principal-screen','children')],[Input('url', 'pathname'), Input('url','href')])
def display_page(pathname,url):
    return [html.Div(html.H1('¡Bienvenido!',style={'color':'rgb(0,0,0)','padding-top':20}),style= {'text-align':'center','padding-bottom':1000})]

if __name__ == '__main__':
    app.run_server(debug = True)