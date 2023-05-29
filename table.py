from dash import Dash, html
import pandas as pd

data = pd.read_csv('Non-stateWarData_v4.0.csv')

df = pd.DataFrame(data)

#df['TotalCombatDeaths'] = df['TotalCombatDeaths'].astype (int)

#df = df[['WarName', 'StartYear', 'EndYear', 'TotalCombatDeaths']]

#df = df[df.TotalCombatDeaths > 0]

def generate_table(dataframe, max_rows=62):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = Dash(__name__)

app.layout = html.Div([
    html.H4(children='List of wars'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)