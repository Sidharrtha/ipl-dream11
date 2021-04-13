# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 00:39:51 2021

@author: Hp User
"""

import pandas as pd
import squad
import numpy as np

df = pd.read_excel('career_2008_2019.xlsx')
df.rename(columns={'Player': 'Player_name'}, inplace=True)

player_lst = squad.squad_list()
#
df.Player_name = df.Player_name.str.replace(' ', '')
player_lst.Player_name = player_lst.Player_name.str.replace(' ', '')
df3 = df.merge(player_lst, on='Player_name', how='inner')
#
#df3['consistency'] = df3['consistency'].replace(-np.inf, 0)

def strike_rate(df):

    if (df['SR'] >= 170):
        return 6
    elif (df['SR'] >= 150.01):
        return 4
    elif (df['SR'] >= 130.01):
        return 2
    elif (df['SR'] >= 60.01 and df['SR'] < 70):
        return -2
    elif (df['SR'] >= 50.01 and df['SR'] < 60):
        return -4
    elif (df['SR'] < 50):
        return -6
    else:
        return 0
    
# df['point'] = df.apply(strike_rate, axis = 1)


df3['dream_11_points'] = (df3['Runs'] + df3['4s'] + df3['6s']*2 
                         - df3['ducks']*2 + df3[100]*16 + df3[50]*8
                         + df3.apply(strike_rate, axis = 1))

# df = df.sort_values(by = 'dream_11_points',ascending = False)

df3['consistency'] = df3['dream_11_points'] / df3['Inns']
df3['consistency'] = df3['consistency'].replace(-np.inf, 0)

def balls_taken_for_4(df):

    if (df['4s'] > 0):
        return df['Balls Faced']/df['4s']
    else:
        return 0
    
def balls_taken_for_6(df):

    if (df['6s'] > 0):
        return df['Balls Faced']/df['6s']
    else:
        return 0

df3['ball_for_4'] = df3.apply(balls_taken_for_4, axis = 1)
df3['ball_for_6'] = df3.apply(balls_taken_for_6, axis = 1)
