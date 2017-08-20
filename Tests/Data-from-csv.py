import csv
import numpy as np

#with open("../Data/Test_Data/RECS2009/recs2009_public.csv") as csvfile:
with open("/home/adam/GitHub/RedRocksCommunityCollege/Clair-Global-Collab/Data/Test_Data/RECS2009/recs2009_public.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    totrooms = []
    playsta1 = []

    for row in readCSV:
        room_total = row[34]
        playstation = row[246]

        totrooms.append(room_total)
        playsta1.append(playstation)

    print(totrooms)
    print(playsta1)

#Check the types
type(totrooms)
type(playsta1)

#Convert to a numpy array
roomarray = np.delete(np.asarray(totrooms),0,0) #np.delete will remove the name since it is the first entry.
plarray = np.delete(np.asarray(playsta1),0,0)

print(roomarray)
roomarray[0] #Pull the first element of the arr
np.shape(roomarray)

print(plarray)
playsta1[0]
np.shape(plarray)


room = np.array([])

for i in range(0,np.shape(roomarray)[0]):
    d = int(roomarray[i])
    room = np.append(room,d)

np.sum(room)
np.sum(room)/np.shape(roomarray)[0]

games = np.array([])
for i in range(0,np.shape(plarray)[0]):
    d = int(plarray[i])
    if d == -2:
        pass
    else:
        games = np.append(games,d)

#Number of -2 in the playstation list
np.shape(plarray)[0] - np.shape(games)[0]

np.sum(games)
np.sum(games)/np.shape(games)[0]
