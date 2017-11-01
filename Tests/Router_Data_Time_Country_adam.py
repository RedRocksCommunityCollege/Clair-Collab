import pandas as pd

# Reads in pdf.
# nrows = number of rows to read in
# 'error_bad_lines=False' drops rows with a different number of entries than expected
# Prints error for each 'bad_line' ommited
Data_Frame_EventA = pd.read_csv('/media/adam/Samsung_T5/GitHub/Clair-Global-Collab/Data/secure-devices.csv', nrows = 2390 , error_bad_lines=False)

df_Time_Country = Data_Frame_EventA[['time', 'srccountry']]
df_Time_Country = df_Time_Country.dropna(axis=0)
df_Time_Country = df_Time_Country.dropna(axis=1)
df_Time_Country = df_Time_Country[:1996]
df_Time_Country.columns = ['Time', 'Country']
#df_Time_Country.columns = ['Time', 'Country', 'Index']

country_list = df_Time_Country['Country'].unique()
country_dict = {key: i for i, key in enumerate(country_list)}

df_Time_Country['Index'] = df_Time_Country['Country'].map(country_dict)
df_Time_Country['Time'] = df_Time_Country['Time'].str.replace(":","").astype(str)

df_Time_Country.to_csv('/media/adam/Samsung_T5/GitHub/Clair-Global-Collab/Data/Country_Index_DF.csv')

df_Time_Country

df_Time_Country.plot(df_Time_Country['Time'] )
