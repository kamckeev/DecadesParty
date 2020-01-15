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
df2.head()

#good to see the headers. I think its 'Survived', 'sex', 'name', 'age', 'marriage status'
PartyMembers=len(df)
#it should be around 86
