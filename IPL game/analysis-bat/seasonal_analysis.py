# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:22:36 2021

@author: Rajat.Dhawale
"""

import pandas as pd
import squad
import numpy as np

def ipl_seasonal_data():


    
    
    df = pd.read_excel('season_2008-2019.xlsx',sheet_name = 'Bat')
    
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
    
    
    df['dream_11_points'] = (df['Runs'] + df['4s'] + df['6s']*2 
                             - df[0]*2 + df[100]*16 + df[50]*8
                             + df.apply(strike_rate, axis = 1))
    
    # df = df.sort_values(by = 'dream_11_points',ascending = False)
    
    df['consistency'] = df['dream_11_points'] / df['Inns']
    df = df.sort_values(by = 'Season',ascending = True)
    # df = df.sort_values(by = 'consistency',ascending = False)                      
    
    def balls_taken_for_4(df):
    
        if (df['4s'] > 0):
            return df['BF']/df['4s']
        else:
            return 0
        
    def balls_taken_for_6(df):
    
        if (df['6s'] > 0):
            return df['BF']/df['6s']
        else:
            return 0
    
    df['ball_for_4'] = df.apply(balls_taken_for_4, axis = 1)
    df['ball_for_6'] = df.apply(balls_taken_for_6, axis = 1)
    # df = df.sort_values(by = 'ball_for_6')
    
    data = df.loc[(df['ball_for_6']>0) & (df['Runs']>120) & (df['Inns']>3)]
    
    
    
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
    df3_old_data = df3_old_data.drop(['consistency', 'ball_for_4','ball_for_6'], axis = 1)
    df3_old_data['ball_for_4'] = df3_old_data.apply(balls_taken_for_4, axis = 1)
    df3_old_data['ball_for_6'] = df3_old_data.apply(balls_taken_for_6, axis = 1)
    
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
    last_year_data = last_year_data.drop(['Team'], axis = 1)
    last_year_data.rename(columns={'hundreds': 100,'fifties':50,'duck':0,'fours':'4s',
                                   'sixes':'6s','Bat_Ave':'Ave'}, inplace=True)
    
    df3_new_data = df3_new_data.drop(['consistency', 'ball_for_4','ball_for_6'], axis = 1)
    
    df3_new_data = df3_new_data.append(last_year_data)
    df3_new_data = df3_new_data.groupby('Player_name').sum()
    
    df3_new_data['ball_for_4'] = df3_new_data.apply(balls_taken_for_4, axis = 1)
    df3_new_data['ball_for_6'] = df3_new_data.apply(balls_taken_for_6, axis = 1)
    
    df3_new_data['consistency'] = df3_new_data['dream_11_points'] / df3_new_data['Inns']
    df3_new_data = df3_new_data.sort_values(by = 'consistency',ascending=False)
    df3_new_data.reset_index(inplace=True)
    df3_new_data['Season'] = 'New_season'
    
    natinality = dict(zip(df3.Player_name, df3.NATIONALITY))
    df3_new_data['NATIONALITY'] = df3_new_data['Player_name'].map(natinality)
    
    team_name = dict(zip(df3.Player_name, df3.team_name))
    df3_new_data['team_name'] = df3_new_data['Player_name'].map(team_name)
    
    df3_new_data = df3_old_data.append(df3_new_data)
    df3_new_data = df3_new_data[['team_name','Player_name','NATIONALITY','Mat','Inns','NO','Runs','HS',
                       'Ave','BF','SR',100,50,0,'4s','6s','Season',
                       'NO in HS','dream_11_points','ball_for_4',
                       'ball_for_6','consistency']]
    df3_new_data = df3_new_data.sort_values(["team_name", "consistency"],ascending=False)
    df3_new_data.to_csv('complete_seasonal_data.csv',index=False)
    
    return df3_new_data




def ipl_2020():
    last_year_data = pd.read_csv('ipl_bat_ave_2021.csv')
    last_year_data.rename(columns={'Player': 'Player_name'}, inplace=True)
    player_lst = squad.squad_list()
    #
    last_year_data.Player_name = last_year_data.Player_name.str.replace(' ', '')
    player_lst.Player_name = player_lst.Player_name.str.replace(' ', '')
    last_year_data = player_lst.merge(last_year_data, on='Player_name', how='left')
    
    last_year_data = last_year_data.drop(['No.'], axis = 1)
    
    def balls_taken_for_4(last_year_data):
    
        if (last_year_data['fours'] > 0):
            return last_year_data['BF']/last_year_data['fours']
        else:
            return 0
        
    def balls_taken_for_6(last_year_data):
    
        if (last_year_data['sixes'] > 0):
            return last_year_data['BF']/last_year_data['sixes']
        else:
            return 0
        
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
        
    last_year_data = last_year_data.replace(np.nan, 0)
    last_year_data = last_year_data.replace('-', 0)
    last_year_data.fours = last_year_data.fours.astype(int)
    last_year_data.sixes = last_year_data.sixes.astype(int)
    last_year_data['Inns'] = last_year_data['Inns'].astype(int)
    last_year_data['BF'] = last_year_data['BF'].astype(int)
    last_year_data['SR'] = last_year_data['SR'].astype(float)
    last_year_data['Runs'] = last_year_data['Runs'].astype(int)
    last_year_data['duck'] = last_year_data['duck'].astype(int)
    last_year_data['hundreds'] = last_year_data['hundreds'].astype(int)
    last_year_data['fifties'] = last_year_data['fifties'].astype(int)
    
    
#    last_year_data['ball_for_4'] = last_year_data.apply(balls_taken_for_4, axis = 1)
#    last_year_data['ball_for_6'] = last_year_data.apply(balls_taken_for_6, axis = 1)
    
    last_year_data['dream_11_points'] = (last_year_data['Runs'] + last_year_data['fours'] 
                                         + last_year_data['sixes']*2 
                                         - last_year_data['duck']*2 + last_year_data['hundreds']*16 
                                         + last_year_data['fifties']*8
                                         + last_year_data.apply(strike_rate, axis = 1))
    
#    last_year_data['consistency'] = last_year_data['dream_11_points'] / last_year_data['Inns']
#    last_year_data = last_year_data.sort_values(by = 'consistency',ascending=False)
    
    return last_year_data



