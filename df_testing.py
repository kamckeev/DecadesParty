TIMESTAMP: 10:52AM-11:00AM
import pandas as pd
import numpy as np
df=pd.read_csv('donner_party1.csv')

type(df)
type(df) is a DataFrame
#I don't know the answer, but I think its false

df2=pd.DataFrame.from_csv('donner_party1.csv')
type(df2)
type(df2) is a DataFrame
#I hope this part is true
#What do you want to do with the dataset now?
donner_df=
#donner_df will be which ever is actually a df

#good to see the headers. I think its 'Survived', 'sex', 'name', 'age', 'marriage status'
PartyMembers=len(df)
#it should be around 86

TIMESTAMP: 11:05AM to 11:17AM
#Determine amount of survivors, percentage of males/females survived

Survive=donner_df[['Survived']].sum()
