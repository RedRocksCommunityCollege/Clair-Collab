import pandas as pd
import plotly as py
from plotly.graph_objs import Scatter, Layout
py.offline.init_notebook_mode(connected=True)
#py.tools.set_credentials_file(username='CoryK8nn8dy', api_key='••••••••••')
#py.tools.set_config_file(sharing='public')

df_Country_Code = pd.read_csv('/Coding/Clair-Global-Collab/Data/2014_world_gdp_with_codes.csv',error_bad_lines=False)

code_dict = df_Country_Code.set_index('COUNTRY')['CODE'].to_dict()

print(code_dict)

# Reads in pdf.
# nrows = number of rows to read in
# 'error_bad_lines=False' drops rows with a different number of entries than expected
# Prints error for each 'bad_line' ommited
Data_Frame_EventA = pd.read_csv('C:\Coding\Clair-Global-Collab\Data\secure-devices.csv', nrows = 2390 , error_bad_lines=False)

# Create Data Frame 'Time_Country', drop nan values, drop extra rows not applicable
df_Time_Country = Data_Frame_EventA[['time', 'srccountry']]
df_Time_Country = df_Time_Country.dropna(axis=0)
df_Time_Country = df_Time_Country.dropna(axis=1)
df_Time_Country = df_Time_Country[:1996]

# Assign counting number to each unique country pinged
country_list = df_Time_Country['srccountry'].unique()
country_dict = {key: i for i, key in enumerate(country_list)}

# Create third column of assigned counting numbers
df_Time_Country['Index'] = df_Time_Country['srccountry'].map(country_dict)

# Create fourth column of assigned country codes
df_Time_Country['Code'] = df_Time_Country['srccountry'].map(code_dict)

#Remove semicolons from timestamps
df_Time_Country['time'] = df_Time_Country['time'].str.replace(":","").astype(str)

# Rename columns
df_Time_Country.columns = ['Time', 'Country', 'Index', 'Code']

df_Time_Country.to_csv('C:/Coding/Clair-Global-Collab/Data/Time_Country.csv')

# Display Data Frame
df_Time_Country

#143223
data = [ dict(
        type = 'choropleth',
        locations = df_Time_Country['Code'],
        z = df_Time_Country['Time'],
        text = df_Time_Country['Code'],
        colorscale = [[0,"rgb(5, 10, 172)"],[0.1,"rgb(40, 60, 190)"],[0.4,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = False,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
     ) ]

layout = dict(
    title = 'Countries Pinged',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
                )
        )
    )

fig = dict( data=data, layout=layout )

py.offline.iplot( fig, validate=False, filename='Clair-event-world-map' )


'''The purpose of the code below, which is currently incomplete, is to categorize the countries by continent. Then, create a scatterplot of countries(y-axis) pinged over time(x-axis) where the countries' points are color coded by continent for additional dimensionality within the graph.'''

df_Time_Country.plot(df_Time_Country['Time'] )

import matplotlib.pyplot as plt
import numpy as np

import plotly.plotly as py
import plotly.tools as tls

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

def FindCountry(country):
    df_country = df_Time_Country['Country'].str.contains(country, na = False)
    return(df_Time_Country[df_country])

# Currently only contains countries from this event, needs be updated to include all
Africa = 'Seychelles', 'South Africa'
Asia = 'Japan', 'China', 'India', 'Vietnam', 'Philippines', 'Indonesia', 'Hong Kong', 'Taiwan', 'Malaysia', 'Pakistan', 'Thailand', 'United Arab Emirates', 'Oman', 'Israel'
Europe = 'United Kingdom', 'Netherlands', 'Europe', 'Germany', 'Sweden', 'Spain', 'Norway', 'Greece', 'France', 'Czech Republic', 'Italy', 'Bulgaria', 'Poland', 'Romania', 'Croatia', 'Russian Federation'
North_America = 'United States', 'Canada', 'Mexico'
Oceania = ''
Cen_South_America = ['Columbia', 'Brazil', 'Argentina', 'Chile']
Unknown_Other = 'Reserved'

int(len(Cen_South_America)-1)

#i = 0
def FindContinent(continent):
    for country in continent:
        return(continent)
    #for i in range(0, int(len(continent))):
    #    return(FindCountry(iter(continent[i])))
    #    i = i + 1


FindContinent(Cen_South_America)



colors = ['b', 'c', 'y', 'm', 'r', 'g', 'k', ]

AF = plt.scatter(random(10), random(10), marker='o', color=colors[0]) # Africa
AS  = plt.scatter(random(10), random(10), marker='o', color=colors[1]) # Asia
EU  = plt.scatter(random(10), random(10), marker='o', color=colors[2]) # Europe
NA  = plt.scatter(random(10), random(10), marker='o', color=colors[3]) # North America
OC = plt.scatter(random(10), random(10), marker='o', color=colors[4]) # Oceania
SA = plt.scatter(random(10), random(10), marker='o', color=colors[5]) # Souht and Central America
UNK/OTHER = plt.scatter(random(10), random(10), marker='o', color=colors[6]) # unknown/other

text = iter(['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South/Central America', 'Unknown/Other'])


mpl_fig = plt.gcf()
plotly_fig = tls.mpl_to_plotly( mpl_fig )

for dat in plotly_fig['data']:
    t = text.next()
	dat.update({'name': t, 'text':t})

plotly_fig['layout']['showlegend'] = True
py.plot(plotly_fig)
