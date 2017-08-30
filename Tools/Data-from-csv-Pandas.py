'''Pandas is ideal for mathing .csv files. This code pulls a few columns from the REC2009 Data
(see Data/Test_Data/RECS2009) and makes comparisons on household education level and the number
of gaming consoles in the household'''

import numpy as np
import pandas as pd

# Create a data frame by reading .csv in, using pandas module
'''Adam's filepath'''
#df = pd.read_csv("/home/adam/GitHub/RedRocksCommunityCollege/Clair-Global-Collab/Data/Test_Data/RECS2009/recs2009_public.csv")
'''Cory's filepath'''
df = pd.read_csv("/Users/K8nn8/Google Drive/RRCC DataLab/Clair-Global-Collab/Data/Test_Data/RECS2009/recs2009_public.csv")

# Define variables as pandas data frames that pull metrics from the RECS2009 csv
TOTALRooms = df.TOTROOMS
BEDRooms = df.BEDROOMS
Game1 = df.PLAYSTA1
Game2 = df.PLAYSTA2
Game3 = df.PLAYSTA3
TVNum = df.TVCOLOR
NumHouseMem = df.NHSLDMEM
Education = df.EDUCATION

# Average values from all datapoints in a metric
NumHouseMem.mean()
Education.mean()
TVNum.mean()
BEDRooms.mean()
TOTALRooms.mean()

'''
--Household education level key--
0. No schooling completed
1. Kindergarten to grade 12
2. High school diploma or GED
3. Some college, no degree
4. Associate's degree
5. Bachelor's degree
6. Master's degree
7. Professional degree
8. Doctorate degree
'''

Houses = np.array([[0,0,0,0,0]]) # Make an empty array. We need [0,0,0,0] for the correct shape.
GamerHouses = np.array([[0,0,0,0,0]])
NoGameHouses = np.array([[0,0,0,0,0]])
# Collect up all the series with rooms as the first element,main TV/console as the second, second TV/console-3rd, third TV/console-4th, and Education level-5th.
for i in range(0, TOTALRooms.count()):
    House = np.array([[TOTALRooms[i],Game1[i],Game2[i],Game3[i],Education[i]]]) # Make each of the tuples. This is how we would add more thing that we would like to study.
    Houses =  np.append(Houses, House, axis = 0) # Add them to the new array.
Houses = np.delete(Houses,0,0) # Remove the extra one from the front of the list.

# Find the houses with three consoles hooked up to all the TV's ("GamerHouses").
for i in range(0, np.shape(Houses)[0]):
    if Houses[i][1] == 1 and Houses[i][2] == 1 and Houses[i][3] == 1:
        GamerHouses = np.append(GamerHouses, [Houses[i]], axis = 0)
    else:
        pass
GamerHouses = np.delete(GamerHouses,0,0) # Remove the extra one from the front of the list.
print(GamerHouses[1:4]) # print a sample size matrix

# Find the houses with no consoles hooked up to any TV ("NoGameHouses").
for i in range(0, np.shape(Houses)[0]):
    if Houses[i][1] == 0 and Houses[i][2] == 0 and Houses[i][3] == 0:
        NoGameHouses = np.append(NoGameHouses, [Houses[i]], axis = 0)
    else:
        pass
NoGameHouses = np.delete(NoGameHouses,0,0) # Remove the extra one from the front of the list.

# Find the average education level of GamerHouses.
Sum = 0
for i in range(0,np.shape(GamerHouses)[0]):
    Sum = GamerHouses[i][4] + Sum

Avg = Sum/np.shape(GamerHouses)[0]
print(Avg)

# Find the average education level of NoGameHouses.
Sum2 = 0
for i in range(0,np.shape(NoGameHouses)[0]):
    Sum2 = NoGameHouses[i][4] + Sum2

Avg2 = Sum2/np.shape(NoGameHouses)[0]
print(Avg2)
