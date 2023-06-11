import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load in the total NPS data (1904 - 2022)
tot = pd.read_csv('NPS Total Visitors.csv')

#create a new column in datafram for %change from the previous year
i = tot.shape[0]-1
tot['Change'] = 0
while i > 0: 
   tot['Change'].iloc[i] = (tot['Visitor Count'].iloc[i] - 
                              tot['Visitor Count'][i-1])/tot['Visitor Count'].iloc[i-1]*100
   i = i-1


#load the by park (2000 - 2022) and convert Year & Month columns to date
by_park = pd.read_csv('Annual Visitation By Park.csv', parse_dates= {"Date" : ["Year","Month"]},  keep_date_col=True)

#select only important columns from dataset
by_park = by_park[['ParkName', 'UnitCode', 'ParkType', 'Region', 'State', 'Date', 'Year', 'Month', 'RecreationVisits']]

#change visit from string to integers 
by_park['RecreationVisits'] = by_park['RecreationVisits'].replace(',','', regex=True)
by_park['RecreationVisits'] = by_park['RecreationVisits'].apply(pd.to_numeric)

#output to csv
cwd = os.getcwd()
path1 = cwd + "\Clean Data\AnnualVisits_1900-2022.csv"
path2 = cwd + "\Clean Data\MonthlyVisits_2000-2022.csv"
tot.to_csv(path1, index = False)
by_park.to_csv(path2, index=False)