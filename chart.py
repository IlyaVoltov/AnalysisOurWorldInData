import pandas
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go


data = pandas.read_csv('Non-stateWarData_v4.0.csv')
dataName = data['WarName']
datavalue = data['Outcome']

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H4('Uppsala Conflict'),
    html.P("Select Name of War:"),
    dcc.Dropdown(
        id="dropdown",
        options=dataName,
        #value='Gold',
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"),
    Input("dropdown", "value"))
def display_color(color):
    fig = go.Figure(
        data=go.Bar(y=datavalue, # replace with your own data source
                    marker_color=color))
    return fig


app.run_server(debug=True)