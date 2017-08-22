import csv
import numpy as np

#Reads .csv, establishes comma as delimiter
with open("/Users/K8nn8/Google Drive/RRCC DataLab/Clair-Global-Collab/Data/Test_Data/RECS2009/recs2009_public.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    totrooms = []
    playsta1 = []

    #Identifies column containing total number of rooms and if a video game console is connected to the primary TV
    for row in readCSV:
        room_total = row[34]
        playstation = row[246]

        totrooms.append(room_total)
        playsta1.append(playstation)

    #Prints selected columns
    print(totrooms)
    print(playsta1) #0=no, 1=yes, -2=N/A

#Checks the types
type(totrooms)
type(playsta1)

#Remove all occurences of "-2" values in playsta1from both lists
indices = [i for i, x in enumerate(playsta1) if x == "-2"] #indexes all occurences of "-2"
print(indices)

for i in indices:
    print(totrooms[i])


#########

np.shape(totrooms)[0]

Houses = np.array([])

for i in range(1, np.shape(totrooms)[0]):
    House = np.array([totrooms[i],playsta1[i]]S)
    #print(House)
    Houses = np.append(Houses,np.array([House]))

#np.array([totrooms[1],playsta1[1]])

print(Houses)
Houses[6]

#######

#Convert to a numpy array
roomarray = np.delete(np.asarray(totrooms),0,0) #np.delete will remove the name since it is the first entry.
psarray = np.delete(np.asarray(playsta1),0,0)

print(roomarray)
roomarray[0] #Pull the first element of the array
np.shape(roomarray) #np.shape counts the total number of values in array

print(psarray)
psarray[0]
np.shape(psarray)


rooms = np.array([])
for i in range(0,np.shape(roomarray)[0]):
    d = int(roomarray[i])
    rooms = np.append(rooms,d)

np.sum(rooms) #total number of rooms in all households
np.sum(rooms)/np.shape(roomarray)[0] #avg. number of rooms per household

games = np.array([])
for i in range(0,np.shape(psarray)[0]):
    d = int(psarray[i])
    games = np.append(games,d)

np.sum(games) #total number households with a gaming console connected to their primary TV
(np.sum(games)/np.shape(psarray)[0])*100 #percentage of households with a gaming console on their primary TV
