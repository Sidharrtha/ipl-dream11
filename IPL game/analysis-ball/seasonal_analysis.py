# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:22:36 2021

@author: Rajat.Dhawale
"""

import pandas as pd
import squad
import numpy as np

def ipl_seasonal_data():


    
    
    df = pd.read_excel('season_2008-2019.xlsx',sheet_name = 'Ball')
    
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
        
    # df['point'] = df.apply(strike_rate, axis = 1)
    
    
    df['dream_11_points'] = (df['Wkts']*25 + df['Ct']*8 + df['St']*12
                             + df['4']*8 + df['5']*16 + df['Mdns']*12
                             + df.apply(economy, axis = 1))
    
    # df = df.sort_values(by = 'dream_11_points',ascending = False)
    
    df['consistency'] = df['dream_11_points'] / df['Inns']
    df = df.sort_values(by = 'Season',ascending = True)
    # df = df.sort_values(by = 'consistency',ascending = False)                      
    
    
    #df['Player'] = df['Player'].str.split('(').str.get(0)
    df.rename(columns={'Player': 'Player_name'}, inplace=True)
    
    player_lst = squad.squad_list()
    #
    df.Player_name = df.Player_name.str.replace(' ', '')
    player_lst.Player_name = player_lst.Player_name.str.replace(' ', '')
    df3 = player_lst.merge(df, on='Player_name', how='left')
    #
    df3['consistency'] = df3['consistency'].replace(-np.inf, 0)
    df3 = df3.sort_values(by = 'consistency',ascending=False)
    df3.to_excel('seasonal_analysis.xlsx',engine='xlsxwriter')
    
    df3 = df3.replace(np.nan, 0)
    
    df3_old_data = df3[df3['Season']<2018]
    df3_new_data = df3[df3['Season']>=2018]
    
    
    #############################################################################
    df3_old_data = df3_old_data.groupby('Player_name').sum()
#    df3_old_data = df3_old_data.drop(['consistency', 'ball_for_4','ball_for_6'], axis = 1)
#    df3_old_data['ball_for_4'] = df3_old_data.apply(balls_taken_for_4, axis = 1)
#    df3_old_data['ball_for_6'] = df3_old_data.apply(balls_taken_for_6, axis = 1)
    
    df3_old_data['consistency'] = df3_old_data['dream_11_points'] / df3_old_data['Inns']
    df3_old_data = df3_old_data.sort_values(by = 'consistency',ascending=False)
    df3_old_data.reset_index(inplace=True)
    df3_old_data['Season'] = 'older_season'
    
    natinality = dict(zip(df3.Player_name, df3.NATIONALITY))
    df3_old_data['NATIONALITY'] = df3_old_data['Player_name'].map(natinality)
    
    team_name = dict(zip(df3.Player_name, df3.team_name))
    df3_old_data['team_name'] = df3_old_data['Player_name'].map(team_name)
    
    #############################################################################
    last_year_data = ipl_2020()
#    last_year_data = last_year_data.drop(['Team'], axis = 1)
    last_year_data.rename(columns={'Ball_Ave': 'Ave','four_wkt':'4','five_wkt':'5','fours':'4s'}, inplace=True)
    
    df3_new_data = df3_new_data.drop(['consistency'], axis = 1)
    
    df3_new_data = df3_new_data.append(last_year_data)
    df3_new_data = df3_new_data.groupby('Player_name').sum()
    
#    df3_new_data['ball_for_4'] = df3_new_data.apply(balls_taken_for_4, axis = 1)
#    df3_new_data['ball_for_6'] = df3_new_data.apply(balls_taken_for_6, axis = 1)
    
    df3_new_data['consistency'] = df3_new_data['dream_11_points'] / df3_new_data['Inns']
    df3_new_data = df3_new_data.sort_values(by = 'dream_11_points',ascending=False)
    df3_new_data.reset_index(inplace=True)
    df3_new_data['Season'] = 'New_season'
    
    natinality = dict(zip(df3.Player_name, df3.NATIONALITY))
    df3_new_data['NATIONALITY'] = df3_new_data['Player_name'].map(natinality)
    
    team_name = dict(zip(df3.Player_name, df3.team_name))
    df3_new_data['team_name'] = df3_new_data['Player_name'].map(team_name)
    
    df3_new_data = df3_old_data.append(df3_new_data)
    df3_new_data = df3_new_data[['team_name','Player_name','NATIONALITY','Mat','Inns','Runs','Overs',
                       'SR','St','Wkts','4','5','Season',
                       'Mdns','Econ','Ave',
                       'dream_11_points','consistency']]
    df3_new_data = df3_new_data.sort_values(["dream_11_points", "consistency"],ascending=False)
    df3_new_data.to_csv('complete_seasonal_data.csv',index=False)
    
    return df3_new_data




def ipl_2020():
    last_year_data = pd.read_csv('ipl_ball_ave_2021.csv')
    last_year_data.rename(columns={'Player': 'Player_name'}, inplace=True)
    player_lst = squad.squad_list()
    #
    last_year_data.Player_name = last_year_data.Player_name.str.replace(' ', '')
    player_lst.Player_name = player_lst.Player_name.str.replace(' ', '')
    last_year_data = player_lst.merge(last_year_data, on='Player_name', how='left')
    
    last_year_data = last_year_data.drop(['No.','Team'], axis = 1)
    
    
        
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
    
        
    last_year_data = last_year_data.replace(np.nan, 0)
    last_year_data = last_year_data.replace('-', 0)
#    last_year_data.fours = last_year_data.fours.astype(int)
#    last_year_data.sixes = last_year_data.sixes.astype(int)
    last_year_data['Inns'] = last_year_data['Inns'].astype(int)
    last_year_data['Overs'] = last_year_data['Overs'].astype(float)
    last_year_data['Mdns'] = last_year_data['Mdns'].astype(float)
    last_year_data['Wkts'] = last_year_data['Wkts'].astype(int)
    last_year_data['Econ'] = last_year_data['Econ'].astype(float)
    last_year_data['four_wkt'] = last_year_data['four_wkt'].astype(int)
    last_year_data['five_wkt'] = last_year_data['five_wkt'].astype(int)
    last_year_data['Ct'] = last_year_data['Ct'].astype(int)
    last_year_data['St'] = last_year_data['St'].astype(int)
    
    
#    last_year_data['ball_for_4'] = last_year_data.apply(balls_taken_for_4, axis = 1)
#    last_year_data['ball_for_6'] = last_year_data.apply(balls_taken_for_6, axis = 1)
    
    last_year_data['dream_11_points'] = (last_year_data['Wkts']*25 + last_year_data['Ct']*8
                              + last_year_data['St']* 12
                             + last_year_data['four_wkt']*8 + last_year_data['five_wkt']*16 + last_year_data['Mdns']*12
                             + last_year_data.apply(economy, axis = 1))
    
    
#    last_year_data['consistency'] = last_year_data['dream_11_points'] / last_year_data['Inns']
    last_year_data = last_year_data.sort_values(by = 'dream_11_points',ascending=False)
    
    return last_year_data



