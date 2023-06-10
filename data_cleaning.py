import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load in the total NPS data (1904 - 2022)
tot = pd.read_csv('NPS Total Visitors.csv')

#create a new column in datafram for %change from the previous year
i = tot.shape[0]-2
tot['Change'] = 0
while i > -1: 
    tot['Change'].iloc[i] = (tot['Visitor Count'].iloc[i+1] - 
                              tot['Visitor Count'][i])/tot['Visitor Count'].iloc[i+1]*100

    i = i-1

#load the by park (2000 - 2022)
by_park = pd.read_csv('Annual Visitation By Park.csv')

#select only important columns from dataset
by_park = by_park[['ParkName', 'UnitCode', 'ParkType', 'Region', 'State', 'Year', 'Month', 'RecreationVisits']]

#change visit from string to integers 
by_park['RecreationVisits'] = by_park['RecreationVisits'].replace(',','', regex=True)
by_park['RecreationVisits'] = by_park['RecreationVisits'].apply(pd.to_numeric)