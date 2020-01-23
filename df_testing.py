import pandas as pd
import numpy as np
donner_df=pd.read_csv('donner_party1.csv')

members = donner_df.shape[0]

alive= donner_df['Survived'].sum()
alive_percent=((alive/members).round(4))*100
dead_percent=(((members-alive)/members).round(4))*100

#What would I like next? Create an if/then clause that would pull the average
#age of hte survivors and compare it to the averae age of the dead

#histogram binning by decades of life, double bar demonstrating alive vs. dead by decade

#need to remove the NaN files from the date ranges