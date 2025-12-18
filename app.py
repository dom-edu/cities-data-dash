import pandas as pd 
import plotly.express as px
from dash import Dash, html , dcc , callback, Output, Input

# DATA 
URL = "https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/2014_us_cities.csv"

cities_df = pd.read_csv(URL)

# sort cities by descending (largest pop at top)
cities_df.sort_values(by="pop", ascending=False)

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

# Exercise: Add this graph to our dash app, 
# make a callback function that updates the graph based on the check boxes
# add two more options to the checkboxes called largest 10, smallest 10 cities

# make values different than labels for easier processing
options=[
       {'label': '10 Largest', 'value': 'large-10'},
       {'label': '10 Smallest', 'value': 'small-10'},
       {'label': '5 Largest', 'value': 'large-5'},
       {'label': '5 Smallest', 'value': 'small-5'},
   ]

cb1 = dcc.Checklist(options, 
                     inline=True, 
                     id="cb-1")


# graph to hold bar chart
graph1 = dcc.Graph(id="histo1")

# add layout
app.layout = [
    dd1,
    cb1,
    graph1,
]

@callback(
    Output('histo1','figure'),
    Input('dd-city-sel','value'),
    Input('cb-1', 'value')
)
def update_histo(cities_sel, check_boxes):

    # DEBUG print("Checkboxes", check_boxes)
    filtered_df = pd.DataFrame() 

    # handle case when check boxes is undefined first
    if not check_boxes:
        # default is to filter by dropdown 
        filter_ = cities_df.name.isin(cities_sel)
        filtered_df = cities_df[filter_]

    elif 'large-5' in check_boxes:
        # get top 5
        filtered_df = cities_df[:5]

    elif 'small-5' in check_boxes:
        # get bottom 5 
        filtered_df = cities_df[-5:]

    elif 'small-10' in check_boxes:
        # get bottom 5 
        filtered_df = cities_df[-10:]
    elif 'large-10' in check_boxes:
        # get bottom 5 
        filtered_df = cities_df[:10]

    return px.bar(filtered_df, x='name', y='pop')



if __name__ == '__main__':
    app.run(debug=True)