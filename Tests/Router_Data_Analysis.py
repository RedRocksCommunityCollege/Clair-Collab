import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Prints pyplot visuals in line with code by default
%matplotlib inline
from wordcloud import WordCloud, STOPWORDS



# Reads in pdf.
# nrows = number of rows to read in
# 'error_bad_lines=False' drops rows with a different number of entries than expected
# Prints error for each 'bad_line' ommited
Data_Frame_EventA = pd.read_csv('C:\Coding\Clair-Global-Collab\Data\secure-devices.csv', nrows = 2390 , error_bad_lines=False)


# Lists all unique strings in the 'X_type' column"
Data_Frame_EventA['X_type'].unique()

# Goes to 'X_type' column, finds all strings in column containing a specific value (ex:'traffic'), and then retains entire row in a new DataFrame
# 'na = False' returns 'False' for each 'NaN' in string
traffic = Data_Frame_EventA[Data_Frame_EventA['X_type'].str.contains('traffic', na = False)]
event = Data_Frame_EventA[Data_Frame_EventA['X_type'].str.contains('event', na = False)]
utm = Data_Frame_EventA[Data_Frame_EventA['X_type'].str.contains('utm', na = False)]
X_131072 = Data_Frame_EventA[Data_Frame_EventA['X_type'].str.contains('131072', na = False)]
app_ctrl_all = Data_Frame_EventA[Data_Frame_EventA['X_type'].str.contains('app-ctrl-all', na = False)]
X_262144 = Data_Frame_EventA[Data_Frame_EventA['X_type'].str.contains('262144', na = False)]

def Xtype_find(type):
    Data_Frame_EventA[Data_Frame_EventA['X_type'].str.contains(type, na = False)]

print(Xtype_find('traffic'))

def Xtype_all():
    Xtype_find('traffic')
    Xtype_find('event')
    Xtype_find('utm')
    Xtype_find('131072')
    Xtype_find('app-cntrl-all')
    Xtype_find('262144')

print(Xtype_all())


'''Maps Countries over time'''

# Identify countries, create list of unique countries, create dictionary to index them
print(Data_Frame_EventA['srccountry'].head())
country = Data_Frame_EventA['srccountry']
country_index = country.unique()
len(country_index)
list(country_index)
country_dict = {key: i for i, key in enumerate(country_index)}
print(country_dict)



# Find time, remove delimiters, make array
print(Data_Frame_EventA['time'].head())
timestamp = np.str(Data_Frame_EventA['time'])
time = np.char.replace(timestamp,':','')
print(time)







'''Evaluates Data in the 'app' column of the 'EventA' DataFrame'''
# Prints all unique values in the 'app' column
print(Data_Frame_EventA['app'].unique())
# Reports total number of unique values in 'app' column
len(Data_Frame_EventA['app'].unique())
# Prints last 5 values in 'app' column
print(Data_Frame_EventA['app'].tail())


# Finds 2nd value ('Microsoft.Portal') in 'app' column of 'Data_Frame_EventA' dataframe, counts its occurences in the entire column, and find the total occurences
int(Data_Frame_EventA['app'].str.count(str(Data_Frame_EventA['app'].unique()[1])).sum())


# Uses a loop to create a flattened array, called 'sites', of each site name and its number of occurences
i = 0
sites = np.array([])
for i in range(25):
    sites = np.append(sites , [Data_Frame_EventA['app'].unique()[i], int(Data_Frame_EventA['app'].str.count(str(Data_Frame_EventA['app'].unique()[i])).sum())])
    i = i + 1


# Pulls, as integer values, the number of occurences of each visited site, and puts them in another flattened array called 'x'
x = sites[1::2].astype(np.int)


# Gives array 'x' a column header 'Visits'
Data_Sites = {'Visits' : x}
# Creates a dataframe using 'Data_Sites' indexed with the site name from the "sites" array
Data_Frame_Sites = pd.DataFrame(Data_Sites, index = sites[::2])
Data_Frame_Sites


# Creates a pie chart of the 'Visits' column of dataframe 'Data_Frame_Sites'
Data_Frame_Sites['Visits'].plot.pie()


# Creates wordle
word_string = (str(Data_Frame_Sites['Visits']))
wordcloud = WordCloud(stopwords=STOPWORDS,
                        background_color='white',
                        width=2400,
                        height=2000,
                        relative_scaling=.5,
                        ).generate(word_string)

plt.imshow(wordcloud)






'''Evaluates Data in the 'app' column of the 'utm' DataFrame'''
# Prints all unique values in the 'app' column
print(utm['app'].unique())
# Reports total number of unique values in 'app' column
len(utm['app'].unique())
# Prints last 5 values in 'app' column
print(utm['app'].tail())


# Finds 4th value ('ISAKMP') in 'app' column of 'utm' dataframe, counts its occurences in the entire column, and find the totalS occurences
int(utm['app'].str.count(str(utm['app'].unique()[3])).sum())


# Uses a loop to create a flattened array, called 'sites', of each site name and its number of occurences
i = 0
sites = np.array([])
for i in range(25):
    sites = np.append(sites , [utm['app'].unique()[i], int(utm['app'].str.count(str(utm['app'].unique()[i])).sum())])
    i = i + 1


# Pulls, as integer values, the number of occurences of each visited site, and puts them in another flattened array called 'x'
x = sites[1::2].astype(np.int)


# Gives array 'x' a column header 'Visits'
Data_Sites = {'Visits' : x}
# Creates a dataframe using 'Data_Sites' indexed with the site name from the "sites" array
Data_Frame_Sites = pd.DataFrame(Data_Sites, index = sites[::2])
Data_Frame_Sites


# Creates a pie chart of the 'Visits' column of dataframe 'Data_Frame_Sites'
Data_Frame_Sites['Visits'].plot.pie()


# Creates wordle
word_string = (str(Data_Frame_Sites['Visits']))
wordcloud = WordCloud(stopwords=STOPWORDS,
                        background_color='black',
                        width=1400,
                        height=1150,
                        mode='RGBA',
                        relative_scaling=.5
                        ).generate(word_string)

plt.imshow(wordcloud)







'''Works in progress'''
len(traffic['srccountry'].unique())

pd.to_numeric(traffic['sentbyte']).sum()
pd.to_numeric(traffic['rcvdbyte']).sum()


print(utm.head())
