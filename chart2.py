import pandas
import plotly.express as px
import plotly.graph_objects as go

data = pandas.read_csv('Non-stateWarData_v4.0.csv')
dataName = data['WarName']
datavalue = data['TotalCombatDeaths']

fig = px.bar(x=dataName, y=datavalue)

fig_widget = go.FigureWidget(fig)
fig_widget

fig.show()