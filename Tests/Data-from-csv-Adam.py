import numpy as np
import pandas as pd

df = pd.read_csv("/home/adam/GitHub/RedRocksCommunityCollege/Clair-Global-Collab/Data/Test_Data/RECS2009/recs2009_public.csv")

Rooms = df.TOTROOMS
Game1 = df.PLAYSTA1
Game2 = df.PLAYSTA2
Game3 = df.PLAYSTA3

Houses = np.array([[0,0,0,0]]) # Make an empty array. We need [0,0] for the correct shape.
GamerHouses = np.array([[0,0,0,0]])
# Collect up all the tuples with rooms as the first element and mainTV as the second.
for i in range(0, Rooms.count()):
    House = np.array([[Rooms[i],Game1[i],Game2[i],Game3[i]]]) # Make each of the tuples. This is how we would add more thing that we would like to study.
    Houses =  np.append(Houses, House, axis = 0) # Add them to the new array.
Houses = np.delete(Houses,0,0) # Remove the extra one from the front of the list.

# Finds the houses with three Systems hooked up to all the TV's.
for i in range(0, np.shape(Houses)[0]):
    if Houses[i][1] == 1 and Houses[i][2] == 1 and Houses[i][3] == 1:
        GamerHouses = np.append(GamerHouses, [Houses[i]], axis = 0)
    else:
        pass
GamerHouses = np.delete(GamerHouses,0,0) # Remove the extra one from the front of the list.

print(GamerHouses)
