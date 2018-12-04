import pandas as pd
import dash_core_components as dcc
import dash
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
from dash.dependencies import Input, Output, State
import plotly
import seaborn
import numpy

#test data
df = pd.read_csv('analyst_activities.csv')

points_plot_df = df[df.Q > 2]

#Create app layout
app = dash.Dash(__name__)
server = app.server
app.layout = html.Div(children=[
html.H1('Analyst Activities'),


dcc.Dropdown(
    id='analyst_dropdown',
    options=[
        {'label': 'Q1','value':1},
        {'label': 'Q2','value':2},
        {'label': 'Q3','value':3},
        {'label': 'Q4','value':4}
    ],
    placeholder="Select a quarter",
),

#histogram
dcc.Graph(
    id='blank',
    figure={'data':[go.Histogram(x=df['Who'])]}
),


#basic graph syntax
dcc.Graph(
    id='mapbox',
    figure = {'data': [go.Bar(x=points_plot_df['Who'],y=points_plot_df['Points'])]}
),

#basic table syntax
dash_table.DataTable(
    id='analyst_table',
    columns = [{"name": i, "id": i} for i in df.columns],
    data=df.to_dict("rows")
)


])

@app.callback(Output('analyst_table', 'data'), [Input('analyst_dropdown', 'value')])
def update_rows(value):
    dff = df[df['Q'] == value]
    return dff.to_dict('records')



#main function
if __name__ == '__main__':
    app.run_server(debug=True)



