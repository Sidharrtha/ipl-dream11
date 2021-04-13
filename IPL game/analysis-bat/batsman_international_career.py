# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 08:10:03 2021

@author: Rajat.Dhawale
"""
def international_data():

    import pandas as pd
    import numpy as np
    
    ipl_players = pd.read_excel('IPL_2021_Squad_List.xlsx',skiprows=2)
    player_lst = pd.DataFrame()
    players_ = pd.DataFrame()
    player_lst['Player_name'] = ipl_players['CSK']
    player_lst['NATIONALITY'] = ipl_players['NATIONALITY']
    player_lst['team_name'] = 'CSK'
    
    players_['Player_name'] = ipl_players['DC']
    players_['NATIONALITY'] = ipl_players['NATIONALITY.1']
    players_['team_name'] = 'DC'
    
    player_lst = player_lst.append(players_, ignore_index = True)
    
    players_['Player_name'] = ipl_players['MI']
    players_['NATIONALITY'] = ipl_players['NATIONALITY.2']
    players_['team_name'] = 'MI'
    
    player_lst = player_lst.append(players_, ignore_index = True)
    
    players_['Player_name'] = ipl_players['KXIP']
    players_['NATIONALITY'] = ipl_players['NATIONALITY.3']
    players_['team_name'] = 'KXIP'
    
    player_lst = player_lst.append(players_, ignore_index = True)
    
    players_['Player_name'] = ipl_players['KKR']
    players_['NATIONALITY'] = ipl_players['NATIONALITY.4']
    players_['team_name'] = 'KKR'
    
    player_lst = player_lst.append(players_, ignore_index = True)
    
    players_['Player_name'] = ipl_players['RR']
    players_['NATIONALITY'] = ipl_players['NATIONALITY.5']
    players_['team_name'] = 'RR'
    
    player_lst = player_lst.append(players_, ignore_index = True)
    
    # players_['Player_name'] = ipl_players['RR']
    # players_['NATIONALITY'] = ipl_players['NATIONALITY.5']
    # players_['team_name'] = 'RR'
    
    # player_lst = player_lst.append(players_, ignore_index = True)
    
    players_['Player_name'] = ipl_players['RCB']
    players_['NATIONALITY'] = ipl_players['NATIONALITY.6']
    players_['team_name'] = 'RCB'
    
    player_lst = player_lst.append(players_, ignore_index = True)
    
    players_['Player_name'] = ipl_players['SRH']
    players_['NATIONALITY'] = ipl_players['NATIONALITY.7']
    players_['team_name'] = 'SRH'
    
    player_lst = player_lst.append(players_, ignore_index = True)
    
    # player_lst = player_lst['Player_name'].dropna()
    # player_lst[player_lst.isna().any(axis=1)]
    # player_lst = player_lst.apply (pd.to_numeric, errors='coerce')
    player_lst = player_lst.dropna(subset=['Player_name'])
    player_lst = player_lst.replace(np.nan, 'IND')
    ##############################################
    
    df = pd.read_csv('t20_bat_5years.csv')
    
    # df1 = df[df.index.isin(df2.index)]
    
    
    df = df.replace(['-'],0)
    df.SR = df.SR.astype('float')
    # df.to_excel('t20_bat_5years.xlsx',engine='xlsxwriter')
    
    df[['Runs', 'fours', 'sixes','duck', 'hundred', 'fifties','Inns']] = df[['Runs', 'fours', 'sixes','duck', 'hundred', 'fifties','Inns']].astype(int)
    # df.to_excel('t20_bat_5years.xlsx',engine='xlsxwriter')
    
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
    
    
    
    
    df['dream_11_points'] = (df['Runs'] + df['fours'] + df['sixes']*2 
                             - df['duck']*2 + df['hundred']*16 + df['fifties']*8
                             + df.apply(strike_rate, axis = 1))
    
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
    df3 = df3.drop(['Unnamed: 0'], axis = 1)
    df3.to_csv('complete_international.csv',index=False)
    return df3
