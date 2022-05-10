#we need to load a file


import pandas as pd

#data=pd.read_csv("bmi.csv",sep="\t")
#if we need to get rid of unnesscary column we using the index in data to csv file not read
#data=pd.read_csv("bmi.csv", index=False ,sep="\t")
data=pd.read_csv("bmi.csv",sep="\t")
print(data)
