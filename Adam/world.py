import plotly as py
import pandas as pd
from plotly.graph_objs import Scatter, Layout
py.offline.init_notebook_mode(connected=True)


df = pd.read_csv('/media/adam/Samsung_T5/GitHub/Clair-Global-Collab/Data/Country_Index_DF.csv',error_bad_lines=False)

data = [ dict(
        type = 'choropleth',
        locations = df['Time'],
        #z = df['Index'],
        text = df['Country'],
        colorscale = [[143223,"rgb(5, 10, 172)"],[143223,"rgb(40, 60, 190)"],[143223,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[143223,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = False,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
     ) ]

layout = dict(
    title = 'Login Country Origin',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
                )
        )
    )

fig = dict( data=data, layout=layout )
fig


py.offline.iplot( fig, validate=False, filename='d3-world-map' )
