import pandas as pd
import numpy as np

# Read in Router_Data(fake).csv
df = pd.read_csv("/Coding/Clair-Global-Collab/Data/Router_Data(fake).csv")

print(df.head())

UserInit = df.user_init
DeviceIP = df.device_ip
ArriveTime = df.arrive_time = df.values
DepartTime = df.depart_time = df.values
BandwidthUsed = df.bandwidth_used
DeviceType = df.device_type
VisitedIP = df.visited_ip
UserRoute = df.user_route

print(DeviceType[[0,1,2,3,4]])

print(ArriveTime[[0,1,2,3,4]],DepartTime[[0,1,2,3,4]])

type(DepartTime)
type(ArriveTime)

DeltaT = (DepartTime-ArriveTime)

print(DeltaT)
