import pandas as pd 
import plotly.express as px
from dash import Dash, html , dcc 

# DATA 
URL = "https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/2014_us_cities.csv"

cities_df = pd.read_csv(URL)


# instantiate dash
app = Dash() 

# COMPONENTS 

# drop down to select cities
dd1 = dcc.Dropdown(cities_df.name, 
                   placeholder="Select city...",
                   id="dd-city-sel",
                   multi=True)

bar_chart = px.bar(cities_df, x='name', y='pop') 

# graph to hold bar chart
graph1 = dcc.Graph(id="histo1", figure=bar_chart)

# add layout
app.layout = [
    dd1,
    graph1,
]

if __name__ == '__main__':
    app.run(debug=True)