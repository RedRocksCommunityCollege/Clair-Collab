
import csv
with open('../Data/Test_Data//RECS2009/recs2009_public.csv') as csvfile:
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
