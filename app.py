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

# graph to hold scatter geo
graph2 = dcc.Graph(id="scattergeo1")
# add layout
app.layout = [
    dd1,
    cb1,
    graph1,
    graph2
]

@callback(
    Output('histo1','figure'),
    Input('dd-city-sel','value'),
    Input('cb-1', 'value')
)
def update_histo(cities_sel, check_boxes):

    new_df = filter_by_checkbox(cities_df, check_boxes, cities_sel)
    return px.bar(new_df, x='name', y='pop')

@callback(
    Output('scattergeo1', 'figure'),
    Input('cb-1', 'value')
)
def update_scatter_geo(check_boxes):
    # make scatter_geo accordingly

    # filter the dataframe by the checkboxes 
    new_df = filter_by_checkbox(cities_df, check_boxes, [])

    # make new geo scatter plot 
    fig = px.scatter_geo(new_df, 
                     lat="lat",
                     lon="lon",
                     size='pop',
                     scope='usa',  
                     color='name', 
                     projection='albers usa') 
    return fig


# HELPER FUNCTIONS  
def filter_by_checkbox(df_, cbs, c_sel):
    """
    Docstring for filter_by_checkbox
    
    :param df_: DataFrame to Filter
    :param cbs: CheckBox Keys 
    """


    # DEBUG print("Checkboxes", check_boxes)
    filtered_df = pd.DataFrame() 

    # handle case when check boxes is undefined first
    if not cbs:
       # default is to filter by dropdown 
        filter_ = df_.name.isin(c_sel)
        filtered_df = cities_df[filter_]
    
    elif 'large-5' in cbs:
        # get top 5
        filtered_df = df_[:5]

    elif 'small-5' in cbs:
        # get bottom 5 
        filtered_df = df_[-5:]

    elif 'small-10' in cbs:
        # get bottom 5 
        filtered_df = df_[-10:]
    elif 'large-10' in cbs:
        # get bottom 5 
        filtered_df = df_[:10]
    
    return filtered_df




if __name__ == '__main__':
    app.run(debug=True)