import pandas as pd


''' This code creates a data frame that could be used to plot countries 'pinged' over time '''


# Read in pdf.
# nrows = number of rows to read in
# 'error_bad_lines=False' drops rows with a different number of entries than expected
# Prints error for each 'bad_line' ommited
Data_Frame_EventA = pd.read_csv('C:\Coding\Clair-Global-Collab\Data\secure-devices.csv', nrows = 2390 , error_bad_lines=False)

# Create Data Frame 'Time_Country', drop nan values, drop extra rows not applicable
df_Time_Country = Data_Frame_EventA[['time', 'srccountry']]
df_Time_Country = df_Time_Country.dropna(axis=0)
df_Time_Country = df_Time_Country.dropna(axis=1)
df_Time_Country = df_Time_Country[:1996]

#Remove semicolons from timestamps, Replace 'Russian Federation' with 'Russia' to match with country code
df_Time_Country['time'] = df_Time_Country['time'].str.replace(":","").astype(str)
df_Time_Country['srccountry'] = df_Time_Country['srccountry'].str.replace("Russian Federation","Russia").astype(str)

# Assign counting number to each unique country pinged
country_list = df_Time_Country['srccountry'].unique()
country_dict = {key: i for i, key in enumerate(country_list)}

# Create third column of assigned counting numbers
df_Time_Country['Index'] = df_Time_Country['srccountry'].map(country_dict)

# Create fourth column of assigned country codes
df_Time_Country['Code'] = df_Time_Country['srccountry'].map(code_dict)

# Rename columns
df_Time_Country.columns = ['Time', 'Country', 'Index', 'Code']

# Write data frame to file location below
df_Time_Country.to_csv('C:/Coding/Clair-Global-Collab/Data/Time_Country.csv')

df_Time_Country
