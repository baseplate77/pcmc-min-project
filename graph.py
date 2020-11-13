
import plotly.graph_objects as go
import plotly.io as plt_io
import pandas as pd

# themeing


# dataframe
pcmc_data = pd.read_csv('pcmc-count-update-2.csv')
pie_age_data = pd.read_csv('age_count_2.csv')
pie_gender_data = pd.read_csv("gender_2.csv")
# pcmc day wise graph

pcmc_graph = go.Figure()
pcmc_graph.add_trace(go.Scatter(x=pcmc_data["date"], y=pcmc_data["DAY WISE PROGRESSIVE POSITIVE COVID CASES"], fill='tozeroy', mode="lines+markers", name='DAY WISE PROGRESSIVE POSITIVE COVID CASES',
                                marker=dict(
    color="#B5B5B5",
    opacity=0.5,)))
pcmc_graph.add_trace(go.Scatter(x=pcmc_data["date"], y=pcmc_data["DAY WISE POSITIVE COVID CASES"], fill='tozeroy', mode="lines+markers", name="DAY WISE POSITIVE COVID CASES",
                                marker=dict(
    color="#31A889",
    opacity=0.5,)))  # fill down to xaxis

pcmc_graph.add_trace(go.Scatter(x=pcmc_data["date"], y=pcmc_data["DAY WISE RECOVERED COVID CASES"], fill='tozeroy', mode="lines+markers", name="DAY WISE RECOVERED COVID CASES",
                                marker=dict(
    color="#ED708B",
    opacity=0.5,)))
pcmc_graph.update_traces(marker=dict(size=6,
                                     line=dict(width=1)))
pcmc_graph.update_layout(hovermode="x unified",
                         hoverlabel=dict(bgcolor="#636362",
                                         font_color="white"),
                         legend=dict(orientation="h", yanchor="bottom",
                                     y=1.02, xanchor="right", x=1),
                         template="simple_white")
# plt_io..update({'paper_bgcolor': 'rgba(0,0,0,0)',
#                                            'plot_bgcolor': 'rgba(0,0,0,0)'})

# ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]

# pcmc_graph.layout.plot_bgcolor = '#262529'
# pcmc_graph.layout.paper_bgcolor = '#262529'

# pcmc_graph.show(config={"hovermode ": "compare"})


# chagne graph background color
# pcmc_graph
pcmc_graph.layout.plot_bgcolor = '#fff'

# pie chart


pie_age_chart = go.Figure(
    data=[go.Pie(values=pie_age_data['count'], labels=pie_age_data["cat"])])
pie_age_chart.update_traces(hoverinfo='label+value', textinfo='value', textfont_size=20,
                            marker=dict(line=dict(color='#ffffff', width=2)))
pie_age_chart.update_layout(hovermode="x unified",
                            hoverlabel=dict(bgcolor="#636362",
                                            font_color="white", font_family="Arial"),
                            legend=dict(orientation="h", yanchor="bottom",
                                        y=1.02, xanchor="right", x=1),
                            template="simple_white")


pie_gender_chart = go.Figure(
    data=[go.Pie(labels=pie_gender_data['cat'], values=pie_gender_data["count"], hole=.5)])
pie_gender_chart.update_traces(hoverinfo='label+value', textinfo='value', textfont_size=20,
                               marker=dict(line=dict(color='#ffffff', width=2)))
pie_gender_chart.update_layout(hovermode="x unified",
                               #                         hoverlabel=dict(bgcolor="#636362",
                               #                                         font_color="white", font_family="Arial"),
                               legend=dict(orientation="h", yanchor="bottom",
                                           y=1.02, xanchor="right", x=1),
                               template="simple_white")


# --------------------------------------- dummy ----------------------
pcmc = go.Figure()
pcmc.add_trace(go.Scatter(x=pcmc_data["date"], y=pcmc_data["DAY WISE PROGRESSIVE POSITIVE COVID CASES"], fill='tozeroy', mode="lines+markers", name='DAY WISE PROGRESSIVE POSITIVE COVID CASES',
                          marker=dict(
    color="#B5B5B5",
    opacity=0.5,)))
# pcmc.add_trace(go.Scatter(x=pcmc_data["date"], y=pcmc_data["DAY WISE POSITIVE COVID CASES"], fill='tozeroy', mode="lines+markers", name="DAY WISE POSITIVE COVID CASES",
#                                 marker=dict(
#     color="#31A889",
#     opacity=0.5,)))  # fill down to xaxis

# pcmc.add_trace(go.Scatter(x=pcmc_data["date"], y=pcmc_data["DAY WISE RECOVERED COVID CASES"], fill='tozeroy', mode="lines+markers", name="DAY WISE RECOVERED COVID CASES",
#                                 marker=dict(
#     color="#ED708B",
#     opacity=0.5,)))
pcmc.update_traces(marker=dict(size=0,
                               line=dict(width=0)))
pcmc.update_layout(hovermode="x unified",
                   hoverlabel=dict(bgcolor="#636362",
                                   font_color="white"),
                   legend=dict(orientation="h", yanchor="bottom",
                               y=1.02, xanchor="right", x=1),
                   template="simple_white")


pcmc_pos_rec = go.Figure()
pcmc_pos_rec.add_trace(go.Scatter(x=pcmc_data["date"], y=pcmc_data["DAY WISE POSITIVE COVID CASES"], fill='tozeroy', mode="lines+markers", name="DAY WISE POSITIVE COVID CASES",
                                  marker=dict(
    color="#d7385e",
    opacity=0.5,)))  # fill down to xaxis

pcmc_pos_rec.add_trace(go.Scatter(x=pcmc_data["date"], y=pcmc_data["DAY WISE RECOVERED COVID CASES"], fill='tozeroy', mode="lines+markers", name="DAY WISE RECOVERED COVID CASES",
                                  marker=dict(
    color="#f6830f",
    opacity=0.5,)))
pcmc_pos_rec.update_traces(marker=dict(size=0,
                                       line=dict(width=0)))

pcmc_pos_rec.update_layout(hovermode="x unified",
                           hoverlabel=dict(bgcolor="#636362",
                                           font_color="white"),
                           legend=dict(orientation="h", yanchor="bottom",
                                       y=1.02, xanchor="right", x=1),
                           template="simple_white")
