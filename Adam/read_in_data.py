import pandas as pd
import numpy as np
import matplotlib
%matplotlib

def Read_File():
    return pd.read_csv('/home/adam/GitHub/RedRocksCommunityCollege/Clair-Global-Collab/Data/secure-devices.csv', nrows = 2390 , error_bad_lines=False)

def Country_Count(Event):
    j = 0
    Country_DF = Event[pd.notnull(Event['srccountry'])]
    Country_DF['srccountry'].unique()
    country = np.array([])
    for j in range(51):
        country = np.append(country , [Country_DF['srccountry'].unique()[j], int(Country_DF['srccountry'].str.count(str(Country_DF['srccountry'].unique()[j])).sum())])
        j = j + 1

    return(country)

def X_type_Function(element,Local_Frame):
    return Local_Frame[Local_Frame['X_type'].str.contains(element, na = False)]

Event_A = Read_File()
Country_Count(Event_A)
X_type_Function('traffic',Event_A)

lData_Frame_EventA['time'][0].replace(":", "")

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


x = country[1::2].astype(np.int)

Data_Country = {'Country' : x}
Data_Frame_Country = pd.DataFrame(Data_Country, index = country[::2])
Data_Frame_Country

Data_Frame_Country['Country'].plot.pie()


Data_Frame_EventA['X_type'].unique()



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
