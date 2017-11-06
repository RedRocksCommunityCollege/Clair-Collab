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
