import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# Read in Router_Data(fake).csv
df = pd.read_csv("/Coding/Clair-Global-Collab/Data/Router_Data(fake).csv")

# Checks first five values
print(df.head())

# Sets df column names
UserInit = df.user_init
DeviceIP = df.device_ip
ArriveTime = df.arrive_time
DepartTime = df.depart_time
BandwidthUsed = df.bandwidth_used
DeviceType = df.device_type
VisitedIP = df.visited_ip
UserRoute = df.user_route

i = 0
Difference = np.array([])
while i in range(0,50000):
    Difference = np.append(Difference, int(ArriveTime[i].replace('1:','')) - int(DepartTime[i].replace('2:','')))
    i = i + 1

Difference



# Creates second data frame, "Time," that is a numpy array of arr/dep times
df_Arr = pd.DataFrame(np.array(df.arrive_time))
#df_Dep = pd.DataFrame(np.array(df[['depart_time']]))

Arr = pd.to_numeric(ArriveTime)
df_Dep = np.array(df.depart_time)

type(Arr)
print(Arr[0,1,2,3,4])
np.shape(Arr)

print(df_Arr.head())

type(df_Arr)

# Checks first five device types
print(DeviceType.head())

'''not working'''
# Checks first five arrival times
#print(ArriveTime())

type(DepartTime)
type(ArriveTime)

print(ArriveTime[1,2,3])

'''not working'''
#DeltaT = (DepartTime-ArriveTime)
#print(DeltaT)

'''not working'''
#df['ArriveTime','DepartTime'].plot()
#plt.show(ArriveTime,DepartTime)
