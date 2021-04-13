# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 08:10:03 2021

@author: Rajat.Dhawale
"""

import squad
import pandas as pd
import numpy as np


def international_data():

    
    player_lst = squad.squad_list()
    
    ##############################################
    
    df = pd.read_csv('t20_bowling_5years.csv')
    
    # df1 = df[df.index.isin(df2.index)]
    
    
    df = df.replace(['-'],0)
#    df.SR = df.SR.astype('float')
    # df.to_excel('t20_bat_5years.xlsx',engine='xlsxwriter')
    df = df.drop(['Span'], axis = 1)
    df[['BBI']] = df[['BBI']].astype(str)
    df[['Ave','Econ','SR','Overs']] = df[['Ave','Econ','SR','Overs']].astype(float)
    df[['Mat', 'Inns', 'Mdns', 'Runs','Wkts','four','five']] = df[['Mat', 'Inns', 'Mdns', 'Runs','Wkts','four','five']].astype(int)
    # df.to_excel('t20_bat_5years.xlsx',engine='xlsxwriter')
    
    def economy(df):
    
        if (df['Econ'] < 5):
            return 6
        elif (df['Econ'] >= 5 and df['Econ'] < 6):
            return 4
        elif (df['Econ'] >= 6 and df['Econ'] < 7):
            return 2
        elif (df['Econ'] >= 10 and df['Econ'] < 11):
            return -2
        elif (df['Econ'] >= 11 and df['Econ'] < 12):
            return -4
        elif (df['Econ'] > 12):
            return -6
        else:
            return 0
    
    
    
    
    df['dream_11_points'] = (df['Wkts']*25 
                             + df['four']*8 + df['five']*16 + df['Mdns']*12
                             + df.apply(economy, axis = 1))
    
    # df = df.sort_values(by = 'dream_11_points',ascending = False)
    
    df['consistency'] = df['dream_11_points'] / df['Inns']
    # df = df.sort_values(by = 'Season',ascending = True)
    df['Player'] = df['Player'].str.split('(').str.get(0)
    df.rename(columns={'Player': 'Player_name'}, inplace=True)
    
    df.Player_name = df.Player_name.str.replace(' ', '')
    player_lst.Player_name = player_lst.Player_name.str.replace(' ', '')
    df3 = player_lst.merge(df, on='Player_name', how='left')
    
    df3['consistency'] = df3['consistency'].replace(-np.inf, 0)
    #m = df.Player_name.isin(player_lst.Player_name)
    #df3 = player_lst[m]
    
    df3 = df3.replace(np.nan, 0)
    df3 = df3.replace(np.inf, 0)
    df3[['consistency','Ave','Econ','SR','Overs']] = df3[['consistency','Ave','Econ','SR','Overs']].round(decimals=2)
    df3 = df3.drop(['Unnamed: 0'], axis = 1)
    df3 = df3.sort_values(by = 'consistency',ascending = False)
    df3.to_csv('complete_international_bollower.csv',index=False)
    return df3
