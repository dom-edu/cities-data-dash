from dash import Dash, html , dcc 


# instantiate dash
app = Dash() 

# COMPONENTS 

dd1 = dcc.Dropdown(['New York', 'Los Angeles', 'Chicago'], 
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