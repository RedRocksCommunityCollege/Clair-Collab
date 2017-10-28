import pandas as pd

# Reads in pdf.
# nrows = number of rows to read in
# 'error_bad_lines=False' drops rows with a different number of entries than expected
# Prints error for each 'bad_line' ommited
Data_Frame_EventA = pd.read_csv('C:\Coding\Clair-Global-Collab\Data\secure-devices.csv', nrows = 2390 , error_bad_lines=False)

df_Time_Country = Data_Frame_EventA[['time', 'srccountry']]

print((df_Time_Country).head())

df_Time_Country = df_Time_Country.dropna(axis=0)
df_Time_Country = df_Time_Country.dropna(axis=1)

df_Time_Country

df_Time_Country['srccountry'].unique()
country_list = df_Time_Country['srccountry'].unique()

country_dict = {key: i for i, key in enumerate(country_list)}
print(country_dict)

df_Time_Country['index'] = df_Time_Country['srccountry'].map(country_dict)
df_Time_Country
