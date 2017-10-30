import pandas as pd

# Reads in pdf.
# nrows = number of rows to read in
# 'error_bad_lines=False' drops rows with a different number of entries than expected
# Prints error for each 'bad_line' ommited
Data_Frame_EventA = pd.read_csv('C:\Coding\Clair-Global-Collab\Data\secure-devices.csv', nrows = 2390 , error_bad_lines=False)

df_Time_Country = Data_Frame_EventA[['time', 'srccountry']]
df_Time_Country = df_Time_Country.dropna(axis=0)
df_Time_Country = df_Time_Country.dropna(axis=1)
df_Time_Country = df_Time_Country[:1996]

country_list = df_Time_Country['srccountry'].unique()
country_dict = {key: i for i, key in enumerate(country_list)}

df_Time_Country['Index'] = df_Time_Country['srccountry'].map(country_dict)
df_Time_Country['time'] = df_Time_Country['time'].str.replace(":","").astype(str)

df_Time_Country.columns = ['Time', 'Country', 'Index']

df_Time_Country

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
