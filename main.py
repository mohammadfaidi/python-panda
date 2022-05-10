import pandas as pd

column = ["bmw","marcedas","chevloate"]
title_columns = {"name":column,"height":[1.67,1.9,0.25],
                "weight":[54,100,1]
                }
data = pd.DataFrame(title_columns)

print(data)


select_column=data['weight'][1]
#iloc = reperesent row

print(select_column)


select_row = data.iloc[1]
#1   marcedas    1.90     100

print(select_row)

#we care about only weight value

select_row = data.iloc[1]['weight']

print(select_row)


#manipulate dataframe values

bmi = []
#weight / (height**2)

#which means that a data mnuipulation

for i in range(len(data)):
    bmi_score = data["weight"][i]/(data["height"][i]**2)
    bmi.append(bmi_score)

#we want to add bmi to our dictionary  data which contain title_columns

data["bmi"] = bmi

print(data)

#save a dataframe to a file
data.to_csv("bmi.csv")

#we want to remove deleiater , to replace it with big space
#we can also save it as bmi.txt with txt file

data.to_csv("bmi.csv",index=False,sep="\t")









