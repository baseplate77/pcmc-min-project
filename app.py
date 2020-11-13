import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output
from graph import pcmc_graph, pie_age_chart, pie_gender_chart, pcmc, pcmc_pos_rec

# POSITIVE PATIENT STATUS table

table_header = [
    html.Thead(
        html.Tr([html.Th("POSITIVE PATIENT STATUS"), html.Th("COUNTS")]), className="table_head")
]

row1 = html.Tr([html.Td("Asymptomatic"), html.Td(html.P(
    "6352", className="table_item_count"))])
row2 = html.Tr([html.Td("Asymptomatic"), html.Td(html.P(
    "940", className="table_item_count"))])
row3 = html.Tr([html.Td("Critical"), html.Td(html.P(
    "142", className="table_item_count"))])
row4 = html.Tr([html.Td("Ventilator"), html.Td(html.P(
    "94", className="table_item_count"))])

table_body = [html.Tbody([row1, row2, row3, row4])]

table = dbc.Table(table_header + table_body, bordered=True)


# external css
external_stylesheets = [dbc.themes.BOOTSTRAP]

# app
app = dash.Dash(
    __name__, external_stylesheets=external_stylesheets,)
# app layout
app.layout = html.Div([
    html.Div(html.H1("PCMC COVID-19 Tracker"), className="app_heading"),
    html.Div([
        html.Div([
            html.P(["last update on : ", html.Span("20 sept")]),
            dbc.Row([
                dbc.Col(html.Div([html.H3(70140), html.P("Total Positivr Cases")],
                                 className="main_div", style={"backgroundColor": "#e74c3c"})),
                dbc.Col(html.Div([html.H3(421), html.P("Today's Positive")],
                                 className="main_div", style={"backgroundColor": "rgb(255,165,0)"})),
                dbc.Col(html.Div([html.H3(963), html.P("Today's Discharged")],
                                 className="main_div", style={"backgroundColor": "#76D0BA"})),
            ]),
            dbc.Row([
                dbc.Col(html.Div([html.H3(7520), html.P("Active Cases")],
                                 className="main_div", style={"backgroundColor": "#17A2B8"})),
                dbc.Col(html.Div([html.H3(61848), html.P("Recovered")],
                                 className="main_div", style={"backgroundColor": "#66BB6A"})),
                dbc.Col(html.Div([html.H3(1168), html.P("Death")],
                                 className="main_div", style={"backgroundColor": "#95AFC0"})),
            ]),
        ], className="app_pcmc_info"),
        # pie chart

        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H4("COVID-19 Age Group Chart",
                            className="card_title"),
                    dcc.Graph(id="pie_age_chart", figure=pie_age_chart),
                ])
            ], className="card"), md=6, sm=12),
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H4("COVID-19 Gender Wise Cases",
                                className="card_title"),
                        dcc.Graph(id="pie_gender_chart2",
                                  figure=pie_gender_chart),
                    ])
                ], className="card"), md=6, sm=12
            )
        ]),
        # table
        dbc.Col(dbc.Card([
            dbc.Table(table_header + table_body, bordered=False)

        ], className="card"), width=4),

        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H4("COVID-19 PCMC Day Wise Positive Cases",
                            className="card_title"),
                    dcc.Graph(id="pcmc_daywise_graph", figure=pcmc),
                ])
            ], className="card pcmc_graph"), md=6, sm=12),
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H4("COVID-19 PCMC pre Day Cases",
                                className="card_title"),
                        dcc.Graph(id="pcmc_daywise_pos_rec_graph",
                                  figure=pcmc_pos_rec),
                    ])
                ], className="card pcmc_graph"), md=6, sm=12
            )
        ]),

        # dbc.Card([
        #     dbc.CardBody([
        #         html.H4("COVID-19 PCMC Cases",
        #                 className="card_title"),
        #         dcc.Graph(id="pcmc_graph", figure=pcmc_graph),
        #     ])
        # ], className="card pcmc_graph1"),
    ], className="app_body")


])


if __name__ == "__main__":
    app.run_server(debug=True)
