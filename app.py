import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
#import dash_table_experiments as dtable
#import dash_dependencies
#from dash.dependenciest import Input, Output, State
import plotly
import seaborn
import numpy

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')


#Create app layout
app = dash.Dash(__name__)
server = app.server
app.layout



