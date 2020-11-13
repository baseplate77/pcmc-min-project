import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
# table 1
table_header = [
    html.Thead(
        html.Tr([html.Th("POSITIVE PATIENT STATUS"), html.Th("COUNTS")]), className="table_head")
]

t1_row1 = html.Tr([html.Td("Asymptomatic"), html.Td(html.P(
    "6352", className="table_item_count"))])
t1_row2 = html.Tr([html.Td("Symptomatic"), html.Td(html.P(
    "940", className="table_item_count"))])
t1_row3 = html.Tr([html.Td("Critical"), html.Td(html.P(
    "142", className="table_item_count"))])
# t1_row4 = html.Tr([html.Td("Ventilator"), html.Td(html.P(
#     "94", className="table_item_count"))])

table_body = [html.Tbody([t1_row1, t1_row2, t1_row3])]

table = dbc.Table(table_header + table_body, bordered=False)

# table 2

table2_header = [
    html.Thead(
        html.Tr([html.Th("NON-PCMC RESIDENTS"), html.Th("COUNTS")]), className="table_head")
]

t2_row1 = html.Tr([html.Td("Active Cases"), html.Td(html.P(
    "6352", className="table2_item_count"))])
t2_row2 = html.Tr([html.Td("Recovered"), html.Td(html.P(
    "940", className="table2_item_count"))])
t2_row3 = html.Tr([html.Td("Death"), html.Td(html.P(
    "142", className="table2_item_count"))])

table2_body = [html.Tbody([t2_row1, t2_row2, t2_row3])]

table2 = dbc.Table(table2_header + table2_body, bordered=False)

# symptoms
s_header = [
    html.Thead(
        html.Th("SYMPTOMS"), className="s_head")
]

s_row1 = html.Tr(html.Td(
    "Active Cdfdfafadfafadfadfadfadfadfadfadfadfdafadfadases", className="s_row"))
s_row2 = html.Tr(html.Td("Active Cases", className="s_row"))
s_row3 = html.Tr(html.Td("Active Cases", className="s_row"))

s_body = [html.Tbody([s_row1, s_row2, s_row3])]

symptoms = dbc.Table(s_header + s_body, bordered=False)


# state list

sl_header = [
    html.Thead(
        html.Tr([html.Th("STATE NAME"), html.Th("COUNTS")]), className="table_head")
]

sl_row1 = html.Tr([html.Td("Active Cases"), html.Td(html.P(
    "6352", className="table2_item_count"))])
sl_row2 = html.Tr([html.Td("Recovered"), html.Td(html.P(
    "940", className="table2_item_count"))])
sl_row3 = html.Tr([html.Td("Death"), html.Td(html.P(
    "142", className="table2_item_count"))])

sl_body = [html.Tbody([sl_row1, sl_row2, sl_row3])]

stateList = dbc.Table(sl_header + sl_body, bordered=False)
