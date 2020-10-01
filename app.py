import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import indexString
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import Home

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],suppress_callback_exceptions=True)
server = app.server
app.title = 'MAC 1152'
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
                                    dbc.DropdownMenu(
                                                                children=[
                                                                    dbc.DropdownMenuItem("Home", header=True),
                                                                    dbc.DropdownMenuItem("Resumen", href="/home"),
                                                                    dbc.DropdownMenuItem("Álgebra", href="/algebra"),
                                                                    dbc.DropdownMenuItem("Cálculo", href="/calculo"),
                                                                    dbc.DropdownMenuItem("Programación", href="/programcion"),
                                                                    dbc.DropdownMenuItem("OdC", href="/organizacion"),
                                                                    dbc.DropdownMenuItem("SAP", href="/solucion"),
                                                                    dbc.DropdownMenuItem("Lógica", href="/logica"),
                                                                ],
                                                                #nav=True,
                                                                in_navbar=True,
                                                                #label="More",
                                                                style = {'padding-left':120},
                                                                label="Selecciona un curso", right=True,
                                                                color="primary", className="m-1"
                                                ),
                                ],
                                color="dark",
                                dark=True,
                                sticky = 'top'
                            ),
                    html.Div(id = 'principal-screen',style = {'background-color':color_fondo})
                    ])

@app.callback([Output('principal-screen','children')],[Input('url', 'pathname'), Input('url','href')])
def display_page(pathname,url):
    if '/home'== pathname or '/'==pathname:
        return  [Home.home]
                
def toggle_modal(pathname, n2, is_open):
    if pathname =='/home' or '/'==pathname:
        return not is_open
    return is_open

app.callback(
    Output("modal-lg", "is_open"),
    [Input("url", "pathname"), Input("close-lg", "n_clicks")],
    [State("modal-lg", "is_open")],
)(toggle_modal)

if __name__ == '__main__':
    app.run_server(debug = True)