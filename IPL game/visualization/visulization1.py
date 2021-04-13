# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:51:59 2021

@author: Rajat.Dhawale
"""


import pandas as pd
# import numpy as np

df = pd.read_excel('seasonal_analysis.xlsx')

data = pd.DataFrame()

data['Season'] = df['Season'].astype(int)

data['Player'] = df['Player']

data['Runs'] = df['Runs']

# data_ = pd.DataFrame()
data_list = {'Player': data.Player.unique()}
data_ = pd.DataFrame(data_list)

def columns_creation(year):
    data_[year] = ''
    
for year in range(2008,2020):
    columns_creation(year)
    

              
def run_score(year):
    pk = data[data['Season']==year]
    for index , row in  pk.iterrows():
        index = data_.index[(data_['Player'] == row['Player'])]
        # print(index)
        data_.loc[index,year] = row['Runs']

for year in range(2008,2020):
    run_score(year)

# data_ = data_.groupby('Player').first()
data = data_
list_of_names = data['Player'].to_list()
data = data.drop('Player',axis='columns', inplace=False)
# data = data.astype(int)
data = data.replace(to_replace ="",
                 value =0)
data = data.cumsum(axis = 1)

idx = 0

data.insert(loc=idx, column='Player', value=list_of_names)

data.to_csv('output1.csv')

col_Names=["Player", "image_url", "2008", "2009","2010", "2011","2012","2013",
          "2014","2015","2016","2017","2018","2019" ]
# my_CSV_File= pd.read_csv("yourCSVFile.csv",names=col_Names)
data = pd.read_csv('output1.csv',names=col_Names)
data.to_csv('output1.csv')


