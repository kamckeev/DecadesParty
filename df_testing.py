TIMESTAMP: 30min on 1-15-2020
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
#it should be 86

#Determine amount of survivors, percentage of males/females survived
Alive=donner_df[['Survived']].sum()
##should be 48

TIMESTAMP: 8:42am to 8:50am on 1-16-2020
Survived=Alive/PartyMembers
Deceased=(PartyMembers-Alive)/PartyMembers

#What are the details on the the deceased? Means of death? Consumed?
#Want to categorize by sex, age of those represnted on the party
#Narrative for the story of the donner party
##Timeline of deaths
##Timeline of rescue
###They definently ate at least one party member. They also killed to American Indians for their flesh.
####Gross
