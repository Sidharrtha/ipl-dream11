# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:48:50 2021

@author: Rajat.Dhawale
"""

import pandas as pd


df1 = pd.read_csv('IPL Ball-by-Ball 2008-2020.csv')

df2 = pd.read_csv('IPL Matches 2008-2020.csv')

new_data1 = pd.DataFrame()
new_data1['id'] = df1['id']
new_data1['total_runs'] = df1['total_runs']


new_data1 = df1.copy()

new_data1.drop(['batsman','non_striker','bowler',
                'player_dismissed', 'fielder', 'extras_type',
                'batting_team', 'bowling_team',
                'dismissal_kind'], axis='columns', inplace=True)

total_runs = pd.DataFrame()
total_runs = new_data1[['id', 'inning','total_runs']]
total_runs = total_runs.groupby(['id','inning'])['total_runs'].agg('sum').reset_index()

def inning1_runs (row):
   if row['inning'] == 1 :
      return row['total_runs']
  
def inning2_runs (row):
   if row['inning'] == 2 :
      return row['total_runs']

total_runs['inning1_runs'] = total_runs.apply (lambda row: inning1_runs(row), axis=1)
total_runs['inning2_runs'] = total_runs.apply (lambda row: inning2_runs(row), axis=1)

total_runs.drop(['inning','total_runs'], axis='columns', inplace=True)
total_runs = total_runs.fillna(0)
total_runs = total_runs.groupby(['id']).sum().reset_index()
total_runs = total_runs.astype(int)
total_runs['total_runs'] = total_runs.inning1_runs + total_runs.inning2_runs
total_runs['winning_margin'] = total_runs.inning1_runs - total_runs.inning2_runs
total_runs['winning_margin'] = total_runs['winning_margin'].abs()

shubham = '8859490837'
