import pandas as pd
import plotly as py
import numpy as np
from plotly.graph_objs import Scatter, Layout
py.offline.init_notebook_mode(connected=True)

# Read in 'EventA' and 'world gdp' pdf.
# nrows = number of rows to read in (2390 are rows from "EventA")
# 'error_bad_lines=False' drops rows with a different number of entries than expected
# Prints error for each 'bad_line' ommited
df_EventA = pd.read_csv('https://raw.githubusercontent.com/RedRocksCommunityCollege/Clair-Collab/master/Data/secure_devices.csv', nrows = 2390 , error_bad_lines=False)
df_GDP = pd.read_csv('https://raw.githubusercontent.com/RedRocksCommunityCollege/Clair-Collab/master/Data/2014_world_gdp_with_codes.csv',error_bad_lines=False)

# Create Data Frame 'Time_Country', drop nan values, drop extra rows not applicable
df_Time_Country = df_EventA[['srccountry']]
df_Time_Country = df_Time_Country.dropna(axis=0)
df_Time_Country = df_Time_Country.dropna(axis=1)

# Replace 'Russian Federation' with 'Russia' to match 'srccountry' value with country codes from '2014_world_gdp_with_codes.csv' value
# NEED TO LOOK FOR OTHER MISMATCHES LIKE THIS ONE
df_Time_Country['srccountry'] = df_Time_Country['srccountry'].str.replace("Russian Federation","Russia").astype(str)

# Drop 'GDP' column
df_Choropleth = df_GDP.drop(['GDP (BILLIONS)'],axis=1)

# Count occurences of each country 'pinged' at event
Country_Counts = df_Time_Country['srccountry'].value_counts()

# Add a column called 'Count' containing country 'ping' occurences
df_Choropleth['Count'] = df_Choropleth['COUNTRY'].map(Country_Counts)

# Make all 'NaN' values (no occurences) zero
df_Choropleth['Count'] = df_Choropleth['Count'].fillna(value=0)

# Rename columns
df_Choropleth.columns = ['Country', 'Code', 'Count']

# Write data frame to file location below
df_Choropleth.to_csv('C:/Coding/Clair-Collab/Data/Countries_Represented.csv')

# Encode data into choropleth
data = [ dict(
        type = 'choropleth',
        locations = df_Choropleth['Code'],
        z = np.log(np.log(df_Choropleth['Count']+1)+1),# Compress values into color range
        text = df_Choropleth['Country'],
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
    title = 'Countries Represented by Attendees',
    geo = dict(
        showframe = False,
        showcoastlines = True,
        projection = dict(
            type = 'Mercator'
                )
        )
    )

fig = dict( data=data, layout=layout )

py.offline.plot( fig, validate=False, filename='Countries_Represented_world_map' )
