import pandas as pd
import numpy as np
import matplotlib
%matplotlib

Data_Frame_EventA = pd.read_csv('/home/adam/GitHub/RedRocksCommunityCollege/Clair-Global-Collab/Data/secure-devices.csv', nrows = 2390 , error_bad_lines=False)

Data_Frame_EventA['time'][0].replace(":", "")

j = 0
TIME_SIG = np.array([])
LOC_SIG = np.array([])
for j in range(0,1999):
    TIME_SIG = np.append(TIME_SIG, int(Data_Frame_EventA['time'][j].replace(":", "")))
    LOC_SIG = np.append(LOC_SIG, Data_Frame_EventA['srccountry'][j])
    j = j + 1

print(TIME_SIG)
Country_DF = Data_Frame_EventA[pd.notnull(Data_Frame_EventA['srccountry'])]

pd.DataFrame(LOC_SIG, index = TIME_SIG)

Country_DF['srccountry'].unique()


j = 0
country = np.array([])
for j in range(51):
    country = np.append(country , [Country_DF['srccountry'].unique()[j], int(Country_DF['srccountry'].str.count(str(Country_DF['srccountry'].unique()[j])).sum())])
    j = j + 1

x = country[1::2].astype(np.int)

Data_Country = {'Country' : x}
Data_Frame_Country = pd.DataFrame(Data_Country, index = country[::2])
Data_Frame_Country

Data_Frame_Country['Country'].plot.pie()


Data_Frame_EventA['X_type'].unique()

traffic = Data_Frame_EventA[Data_Frame_EventA['X_type'].str.contains('traffic', na = False)]
event = Data_Frame_EventA[Data_Frame_EventA['X_type'].str.contains('event', na = False)]
utm = Data_Frame_EventA[Data_Frame_EventA['X_type'].str.contains('utm', na = False)]
X_131072 = Data_Frame_EventA[Data_Frame_EventA['X_type'].str.contains('131072', na = False)]
app_ctrl_all = Data_Frame_EventA[Data_Frame_EventA['X_type'].str.contains('app-ctrl-all', na = False)]
X_262144 = Data_Frame_EventA[Data_Frame_EventA['X_type'].str.contains('262144', na = False)]

int(utm['app'].str.count(str(utm['app'].unique()[3])).sum())

i = 0
sites = np.array([])
for i in range(25):
    sites = np.append(sites , [utm['app'].unique()[i], int(utm['app'].str.count(str(utm['app'].unique()[i])).sum())])
    i = i + 1

x = sites[1::2].astype(np.int)

Data_Sites = {'Visits' : x}
Data_Frame_Sites = pd.DataFrame(Data_Sites, index = sites[::2])
Data_Frame_Sites

Data_Frame_Sites['Visits'].plot.pie()

len(utm['app'].unique())
len(traffic['srccountry'].unique())

pd.to_numeric(traffic['sentbyte']).sum()
pd.to_numeric(traffic['rcvdbyte']).sum()
