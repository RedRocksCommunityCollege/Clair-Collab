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

# Converts lists to ndarrays
ArriveTime = df.values
DepartTime = df.values

# Checks first five device types
print(DeviceType[[0,1,2,3,4]])

'''not working'''
# Checks first five arrival times
print(ArriveTime[[0,1,2,3,4]])

type(DepartTime)
type(ArriveTime)

'''not working'''
#DeltaT = (DepartTime-ArriveTime)
#print(DeltaT)

'''not working'''
#df['ArriveTime','DepartTime'].plot()
#plt.show(ArriveTime,DepartTime)
