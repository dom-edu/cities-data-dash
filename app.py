import pandas as pd 
import plotly.express as px
from dash import Dash, html , dcc , callback, Output, Input

# DATA 
URL = "https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/2014_us_cities.csv"

cities_df = pd.read_csv(URL)

# fix trailing whitespace in 'name'
cities_df.name = cities_df.name.str.strip()

# instantiate dash
app = Dash() 

# COMPONENTS 

# drop down to select cities
dd1 = dcc.Dropdown(cities_df.name, 
                   ['Los Angeles', 'New York'],
                   placeholder="Select city...",
                   id="dd-city-sel",
                   multi=True)

# graph to hold bar chart
graph1 = dcc.Graph(id="histo1")

# add layout
app.layout = [
    dd1,
    graph1,
]

@callback(
    Output('histo1','figure'),
    Input('dd-city-sel','value')
)
def update_histo(cities_sel):
    
    # DEBUG: print("Cities Sel:", cities_sel)
    filter_ = cities_df.name.isin(cities_sel)

    return px.bar(cities_df[filter_], x='name', y='pop')



if __name__ == '__main__':
    app.run(debug=True)