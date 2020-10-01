import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import datetime

def now():
    now = datetime.datetime.now()
    day = now.strftime("%A")

    if day == 'Monday' or day == 'Wednesday' or day =='Friday':
        if (now.hour > 16):
            return [[html.Div(html.H1('Siguiente clase:',style={'color':'rgb(0,0,0)','padding-top':20}),
                            style= {'text-align':'center','margin-bottom':30}),
                dbc.Card( dbc.CardBody(
                            [
                                                html.H5("Álgebra Superior", className="card-title"),
                                                html.P(["Evaluación:",
                                                    html.Br(),
                                                    "- 70% Examen",
                                                    html.Br(),
                                                    "- 30% Tareas"],
                                                    className="card-text",
                                                ),
                                                html.A(
                                                        dbc.Button("Plataforma: Zoom", color="primary"),
                                                        href = 'https://cuaedunam.zoom.us/j/92323338135',
                                                        target = '_blank'
                                                    ),
                                                html.A(
                                                    dbc.Button("Plataforma: SEA", color="primary", style = {'margin':10}),
                                                href = 'https://sea.acatlan.unam.mx/course/view.php?id=4643',
                                                        target = '_blank'
                                                    ),
                            ])
                        )]]
    else:
        return [html.Div(html.H1('Siguiente clase:',style={'color':'rgb(0,0,0)','padding-top':20}))]




home =  [html.Div(html.H1('Resumen de todos los cursos:',style={'color':'rgb(0,0,0)','padding-top':20}),
                style= {'text-align':'center','margin-bottom':30}),
                dbc.Modal([
                                dbc.ModalHeader("Aviso"),
                                dbc.ModalBody("Esta no es una página oficial de la UNAM, fue realizada por un estudiante de MAC ¡Goya!"),
                                dbc.ModalFooter(
                                    dbc.Button("Close", id="close-lg", className="ml-auto")
                                ),
                            ],
                            id="modal-lg",
                            size="lg",
                        ),
                
        html.Div(children=[
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                                        dbc.CardBody(
                                            [
                                                html.H4("Álgebra Superior", className="card-title"),
                                                html.P(["Evaluación:",
                                                    html.Br(),
                                                    "- 70% Examen",
                                                    html.Br(),
                                                    "- 30% Tareas"],
                                                    className="card-text",
                                                ),
                                                html.A(
                                                        dbc.Button("Plataforma: Zoom", color="primary"),
                                                        href = 'https://cuaedunam.zoom.us/j/92323338135',
                                                        target = '_blank'
                                                    ),
                                                html.A(
                                                    dbc.Button("Plataforma: SEA", color="primary", style = {'margin':10}),
                                                href = 'https://sea.acatlan.unam.mx/course/view.php?id=4643',
                                                        target = '_blank'
                                                    ),
                                            ]
                                        ),
                                    ],
                                    #style={"width": "20%"},
                                )
                    ),            
                    dbc.Col(
                        dbc.Card([
                                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                                        dbc.CardBody(
                                            [
                                                html.H4("Cálculo I,", className="card-title"),
                                                html.P(["Evaluación:",
                                                    html.Br(),
                                                    "- 70% Examen",
                                                    html.Br(),
                                                    "- 30% Problemario / Tareas"],
                                                    className="card-text",
                                                ),
                                                html.A(
                                                        dbc.Button("Plataforma: Meet", color="primary"),
                                                        href = 'https://meet.google.com/bcx-zabh-onb',
                                                        target = '_blank'
                                                    ),
                                                html.A(
                                                    dbc.Button("Plataforma: Classroom", color="primary", style = {'margin':10}),
                                                href = 'https://classroom.google.com/u/1/c/MTM4ODE3ODA5ODQ3',
                                                        target = '_blank'
                                                    ),
                                            ]
                                        ),
                                    ],
                                    #style={"width": "20%"},
                                )    
                    )            
                ]),    
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                                        dbc.CardBody(
                                            [
                                                html.H4("Programación", className="card-title"),
                                                html.P(["Evaluación:",
                                                    html.Br(),
                                                    "- ?"],
                                                    #html.Br(),
                                                    #"- 30% Tareas"],
                                                    className="card-text",
                                                ),
                                                html.A(
                                                        dbc.Button("Plataforma: Zoom", color="primary"),
                                                        href = 'https://cuaed-unam.zoom.us/w/95241719089?tk=tTU9n6qF3fMINKxGxZ8b1Bhfb91br8P1PtanV5WLByI.DQIAAAAWLNlNMRZJZkJXdDY4alJ5Q3h4Y3YtRVJiOV9BAAAAAAAAAAAAAAAAAAAAAAAAAAAA#success',
                                                        target = '_blank'
                                                    ),
                                                #html.A(
                                                #    dbc.Button("Plataforma: ?", color="primary", style = {'margin':10}),
                                                #href = '#',
                                                        #target = '_blank'
                                                 #   ),
                                            ]
                                        ),
                                    ],
                                    #style={"width": "20%"},
                                )
                    ),            
                    dbc.Col(
                        dbc.Card([
                                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                                        dbc.CardBody(
                                            [
                                                html.H4("Organización de Computadoras", className="card-title"),
                                                html.P(["Evaluación:",
                                                    html.Br(),
                                                    "- 1 a 2 actividades semanales (tareas y prácticas), con valor de 50%.",
                                                    html.Br(),
                                                    "- 2 Exámenes parciales, con valor de 20%.",
                                                    html.Br(),
                                                    "- 1 Examen final de 1a. Vuelta, con valor de 30%.",
                                                    html.Br(),
                                                    ' ',
                                                    html.Br(),
                                                    "Alternativamente, el examen final de 2a. Vuelta con valor de 100% (no se promedia).",
                                                    html.Br()],
                                                    #"- 30% Problemario / Tareas"],
                                                    className="card-text",
                                                ),
                                                html.A(
                                                        dbc.Button("Plataforma: Zoom", color="primary"),
                                                        href = 'https://cuaed-unam.zoom.us/j/97105209570',
                                                        target = '_blank'
                                                    ),
                                                html.A(
                                                    dbc.Button("Plataforma: SEA", color="primary", style = {'margin':10}),
                                                href = 'https://sea.acatlan.unam.mx/course/view.php?id=4660',
                                                        target = '_blank'
                                                    ),
                                            ]
                                        ),
                                    ],
                                    #style={"width": "20%"},
                                )    
                    )            
                ], style = {'margin-top':30}),
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                                        dbc.CardBody(
                                            [
                                                html.H4("Solución algorítmica de problemas", className="card-title"),
                                                html.P(["Evaluación:",
                                                    html.Br(),
                                                    "- 10% Ejercicios",
                                                    html.Br(),
                                                    "- 20% Examen",
                                                    html.Br(),
                                                    "- 10% Exposición",
                                                    html.Br(),
                                                    "- 10% Algoritmos",
                                                    html.Br(),
                                                    "- 10% Proyecto",
                                                    html.Br(),
                                                    "- 10% Lecturas",
                                                    html.Br(),
                                                    "- 10% Tareas"],
                                                    className="card-text",
                                                ),
                                                html.A(
                                                        dbc.Button("Plataforma: Zoom", color="primary"),
                                                        href = 'https://cuaed-unam.zoom.us/j/97523201907',
                                                        target = '_blank'
                                                    ),
                                                html.A(
                                                        dbc.Button("Plataforma: SEA", color="primary", style = {'margin':10}),
                                                        href = 'https://sea.acatlan.unam.mx/enrol/index.php?id=4677',
                                                        target = '_blank'
                                                    ),
                                                html.A(
                                                        dbc.Button("Plataforma: Dropbox", color="primary", style = {'margin':10, 'margin-left':0}),
                                                        href = 'https://www.dropbox.com/home/SAP',
                                                        target = '_blank'
                                                    ),
                                            ]
                                        ),
                                    ],
                                    #style={"width": "20%"},
                                )
                    ),            
                    dbc.Col(
                        dbc.Card([
                                        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                                        dbc.CardBody(
                                            [
                                                html.H4("Lógica", className="card-title"),
                                                html.P(["Evaluación:",
                                                    html.Br(),
                                                    " - ",
                                                    html.Br()],
                                                    #"- 30% Problemario / Tareas"],
                                                    className="card-text",
                                                ),
                                                html.A(
                                                        dbc.Button("Plataforma: Zoom", color="primary"),
                                                        href = 'https://us04web.zoom.us/j/78915003771?pwd=QU1RdVZZbnk3dWRZRGQzUG5NZno1Zz09',
                                                        target = '_blank'
                                                    ),
                                                html.A(
                                                    dbc.Button("Plataforma: SEA", color="primary", style = {'margin':10}),
                                                href = 'https://sea.acatlan.unam.mx/course/view.php?id=4653',
                                                        target = '_blank'
                                                    ),
                                            ]
                                        ),
                                    ],
                                    #style={"width": "20%"},
                                )    
                    )            
                ], style = {'margin-top':30}),

        ],style= {'width':'70%', 'margin-right':'auto','margin-left':'auto'})
                ]