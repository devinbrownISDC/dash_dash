import pandas as pd
import dash_core_components as dcc
import dash
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
#import dash_dependencies
#from dash.dependenciest import Input, Output, State
import plotly
import seaborn
import numpy

#test data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')


#Create app layout
app = dash.Dash(__name__)
server = app.server
app.layout = html.Div(children=[
html.H1('Hello Dash'),

#basic graph syntax
dcc.Graph(
    id='mapbox',
    figure = {'data': [go.Bar(x=df['Postal'],y=df['Population'])]}
),

#basic table syntax
dash_table.DataTable(
    id='table',
    columns = [{"name": i, "id": i} for i in df.columns],
    data=df.to_dict("rows")
    )
]

)




#main function
if __name__ == '__main__':
    app.run_server(debug=True)



