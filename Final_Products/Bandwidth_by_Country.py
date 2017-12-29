import pandas as pd
import plotly as py
import numpy as np
from plotly.graph_objs import Scatter, Layout
py.offline.init_notebook_mode(connected=True)


df_eventa = pd.read_csv('https://raw.githubusercontent.com/RedRocksCommunityCollege/Clair-Collab/master/Data/secure_devices.csv', nrows = 1999 , error_bad_lines=False)

df_countries_represented = pd.read_csv('https://raw.githubusercontent.com/RedRocksCommunityCollege/Clair-Collab/master/Data/Countries_Represented.csv',error_bad_lines=False)

# Create dictionary linking country names to their country code
code_dict = dict(zip(df_countries_represented.Country, df_countries_represented.Code))

# Create DataFrame
df_countries_bandwidth = pd.DataFrame({'Country': df_eventa['srccountry'], 'Code': df_eventa['srccountry'].map(code_dict), 'Sent Byte': df_eventa['sentbyte'], 'Rcvd Byte': df_eventa['rcvdbyte'], 'Total Byte': (df_eventa['sentbyte'] + df_eventa['rcvdbyte'])})

# Sum the bandwidth values for each country
df_countries_bandwidth = df_countries_bandwidth.groupby(['Country', 'Code'], sort=False).sum()

# Realign column headers after summation
df_countries_bandwidth = df_countries_bandwidth.reset_index()

# Write data frame to file location below
df_countries_bandwidth.to_csv('C:/Coding/Clair-Collab/Data/Countries_Bandwidth.csv')

# Map data to choropleth
data = [ dict(
        type = 'choropleth',
        locations = df_countries_bandwidth['Code'],
        z = np.log(df_countries_bandwidth['Total Byte']+1),# Use log to compress values into color range
        text = df_countries_bandwidth['Country'],
        colorscale = [[0,"rgb(5, 10, 172)"],[.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
                    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
     ) ]

# Set layout of choropleth
layout = dict(
    title = 'Relative Bandwidth by Country',
    geo = dict(
        showframe = False,
        showcoastlines = True,
        projection = dict(
            type = 'Mercator'
                )
        )
    )

fig = dict( data=data, layout=layout )

py.offline.plot( fig, validate=False, filename='Bandwidth_by_Country_world_map' )
