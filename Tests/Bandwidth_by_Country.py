import pandas as pd



df_eventa = pd.read_csv('https://raw.githubusercontent.com/RedRocksCommunityCollege/Clair-Global-Collab/master/Data/secure-devices.csv', nrows = 1999 , error_bad_lines=False)

df_countries_represented = pd.read_csv('https://raw.githubusercontent.com/RedRocksCommunityCollege/Clair-Global-Collab/master/Data/Countries_Represented.csv',error_bad_lines=False)

code_dict = dict(zip(df_countries_represented.Country, df_countries_represented.Code))

df_countries_bandwidth = pd.DataFrame({'Country': df_eventa['srccountry'], 'Code': df_eventa['srccountry'].map(code_dict), 'Sent Byte': df_eventa['sentbyte'], 'Rcvd Byte': df_eventa['rcvdbyte'], 'Total Byte': (df_eventa['sentbyte'] + df_eventa['rcvdbyte'])})

for item in pd.unique(df_countries_bandwidth['Country']):
    i = 0
    Rbyte = 0
    Sbyte = 0
    while i < np.shape(df_countries_bandwidth)[0]:
        if df_countries_bandwidth['Country'][i] == item:
            Rbyte = Rbyte + int(df_countries_bandwidth['Rcvd Byte'][i])
            Sbyte = Sbyte + int(df_countries_bandwidth['Sent Byte'][i])
        else:
            pass
        i  = i + 1


country_str = str(df_countries_bandwidth['Country'].unique)

df_countries_bandwidth.groupby('Country')['Rcvd Byte'].sum()['United States']

df_countries_bandwidth.loc[df_countries_bandwidth['Country'] == 'United States', 'Rcvd Byte'].sum()

df_countries_bandwidth


'''_______________________________ experimentation_____________________________________'''
f_Choropleth['SentBytes'] = pd.Series(df_Choropleth['Country'](0), index=df_Choropleth.index)


df_EventA = df_EventA[:1999]
df_Choropleth = pd.DataFrame({'Country': df_Choropleth['Country'], 'Code': df_Choropleth['Code'], 'Count': df_Choropleth['Count'], 'Rec Byte': df_EventA['rcvdbyte'] ,'Sent Byte': df_EventA['sentbyte']})
Total = np.array(['Total Rec', 'Total Sent'])

for item in pd.unique(df_Choropleth['Country']):
    i = 0
    Rbyte = 0
    Sbyte = 0
    while i < np.shape(df_Choropleth)[0]:
        if df_Choropleth['Country'][i] == item:
            Rbyte = Rbyte + int(df_Choropleth['Rec Byte'][i])
            Sbyte = Sbyte + int(df_Choropleth['Sent Byte'][i])
        else:
            pass
        i  = i + 1
    Total = np.append(Total,[Rbyte,Sbyte])

DataTotals = ({'Country': pd.unique(df_EventA['srccountry']), 'Rec Bytes': Total[2::2] , 'Sent Bytes': Total[3::2]})
df_Choropleth_Bandwidth = pd.DataFrame(DataTotals)
df_Choropleth_Bandwidth

Total


df_Choropleth
'''________________________________end_experimentation________________________________'''
