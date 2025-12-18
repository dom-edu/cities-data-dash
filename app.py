import pandas as pd 
from dash import Dash, html , dcc 

# DATA 
URL = "https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/2014_us_cities.csv"

cities_df = pd.read_csv(URL)


# instantiate dash
app = Dash() 

# COMPONENTS 

dd1 = dcc.Dropdown(cities_df.name, 
                   placeholder="Select city...",
                   id="dd-city-sel",
                   multi=True)

graph1 = dcc.Graph(id="histo1")
graph2 = dcc.Graph(id="histo2")

# add layout
app.layout = [
    dd1,
    graph1,
    graph2
]

if __name__ == '__main__':
    app.run(debug=True)