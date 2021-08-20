#Importing the dependencies
import pandas as pd


raw_data = pd.read_csv(r'london_pollution.csv')

df = pd.DataFrame(raw_data, columns=['Date','Bloomsbury','Barking'])

data_gropued_by_year = df.groupby(pd.to_datetime(df['Date']).map(lambda x: x.year))

#Descriptive statistics
description = data_gropued_by_year.describe()
print(description)

#Calculating the missing values
#missing_calc = data_gropued_by_year.isnull()


for key, item in data_gropued_by_year:
    data_collection = data_gropued_by_year.get_group(key).info()

# Calculated values summarized
#2000 366 entries
#Bloomsbury => 12 null values
#Barking => 3 null values

#2001=> 365 entries
#Bloomsbury => 12 null entries
#Barking => 104 null entries

#2002=> 366 3ntries
#Bloomsbury => 240 null entries
#Barking => 113 null entries

#2003 365 entries
#Bloomsbury => 154 null values
#Barking => 11 null values

#2004=> 366 entries
#Bloomsbury => 9 null entries
#Barking => 1 null entries

'''
The pattern of missing values have drastically changed over a priod of time
It moved from a period of low missing value to high missing values and eventually to low missing values
2000 had a low missing rates, 2002 had the peak of missing values both in Bloomsburry and Barking while 2004 
had the fewest concentration of missing values.
The distribution of missing values is hence relatively symmetric
'''