# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 00:39:51 2021

@author: Hp User
"""

import pandas as pd
import squad
import numpy as np

df = pd.read_csv('IPL Ball-by-Ball 2008-2020.csv')
df.dropna(subset = ["fielder"], inplace=True)
df['fielder_1'] = df['fielder'].str.split(',').str[0]
df['fielder_2'] = df['fielder'].str.split(',').str[1]
df.rename(columns={'fielder_1': 'Player_name'}, inplace=True)

df_copy = df.copy()
df_copy['Player_name'] = ''
df_copy.dropna(subset = ["fielder_2"], inplace=True)
df_copy.rename(columns={'fielder_2': 'Player_name','Player_name': 'fielder_2'}, inplace=True)

data = df.append(df_copy)
#data.dropna(subset = ["fielder_2","fielder"], inplace=True)
data = data.drop(["fielder_2","fielder"], axis = 1)

player_lst = squad.squad_list()
#
data.Player_name = data.Player_name.str.replace(' ', '')
player_lst.Player_name = player_lst.Player_name.str.replace(' ', '')
df3 = player_lst.merge(data, on='Player_name', how='left')

 
fielder_data = pd.DataFrame()
fielder_data['Player_name'] = df3['Player_name']
fielder_data['NATIONALITY'] = df3['NATIONALITY']
fielder_data['team_name'] = df3['team_name']
fielder_data['dismissal_kind'] = df3['dismissal_kind']

fielder_data = fielder_data.groupby(['Player_name', 'dismissal_kind']).count()
fielder_data.reset_index(inplace=True)

