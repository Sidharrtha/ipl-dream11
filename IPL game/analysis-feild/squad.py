# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 00:12:20 2021

@author: Hp User
"""

def squad_list():
    
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
    
    return player_lst