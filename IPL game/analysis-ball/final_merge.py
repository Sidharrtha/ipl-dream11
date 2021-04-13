# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 00:22:28 2021

@author: Hp User
"""

import seasonal_analysis
import batsman_international_career
#import pandas as pd
import squad
import numpy as np


seasonal_data = seasonal_analysis.ipl_seasonal_data()
international_data = batsman_international_career.international_data()

ipl_old_data = seasonal_data[seasonal_data.Season == 'older_season']
ipl_New_data = seasonal_data[seasonal_data.Season == 'New_season']


    
    
#final_data = pd.DataFrame()
data = squad.squad_list() 
data.Player_name = data.Player_name.str.replace(' ', '')

def mapping_columns(df,column,column_name):
    my_dict = dict(zip(df.Player_name, df[column_name]))
    data[column] = data['Player_name'].map(my_dict)

################## Matches #######################################
mapping_columns(international_data,'international_matches','Mat')
mapping_columns(ipl_old_data,'ipl_matches_older','Mat')
mapping_columns(ipl_New_data,'ipl_matches_New','Mat')

################## Innings #######################################
mapping_columns(international_data,'international_Inns','Inns')
mapping_columns(ipl_old_data,'ipl_Inns_older','Inns')
mapping_columns(ipl_New_data,'ipl_Inns_New','Inns')

################## Runs #######################################
mapping_columns(international_data,'international_Overs','Overs')
mapping_columns(ipl_old_data,'ipl_Overs_older','Overs')
mapping_columns(ipl_New_data,'ipl_Overs_New','Overs')

################## highest score #######################################
mapping_columns(international_data,'international_Mdns','Mdns')
mapping_columns(ipl_old_data,'ipl_Mdns_older','Mdns')
mapping_columns(ipl_New_data,'ipl_Mdns_New','Mdns')


################## Batting average #######################################
mapping_columns(international_data,'international_Runs','Runs')
mapping_columns(ipl_old_data,'ipl_Runs_older','Runs')
mapping_columns(ipl_New_data,'ipl_Runs_New','Runs')

################## Balls face #######################################
mapping_columns(international_data,'international_Wkts','Wkts')
mapping_columns(ipl_old_data,'ipl_Wkts_older','Wkts')
mapping_columns(ipl_New_data,'ipl_Wkts_New','Wkts')

################## Strike Rate #######################################
#mapping_columns(international_data,'international_BBI','BBI')
#mapping_columns(ipl_old_data,'ipl_BBI_older','BBI')
#mapping_columns(ipl_New_data,'ipl_BBI_New','BBI')


################## Century  #######################################
mapping_columns(international_data,'international_Ave','Ave')
mapping_columns(ipl_old_data,'ipl_Ave_older','Ave')
mapping_columns(ipl_New_data,'ipl_Ave_New','Ave')



################## fifty  #######################################
mapping_columns(international_data,'international_Econ','Econ')
mapping_columns(ipl_old_data,'ipl_Econ_older','Econ')
mapping_columns(ipl_New_data,'ipl_Econ_New','Econ')



################## ducks  #######################################
#mapping_columns(international_data,'international_ducks','duck')
#mapping_columns(ipl_old_data,'ipl_ducks_older',0)
#mapping_columns(ipl_New_data,'ipl_ducks_New',0)


################## fours  #######################################
mapping_columns(international_data,'international_SR','SR')
mapping_columns(ipl_old_data,'ipl_SR_older','SR')
mapping_columns(ipl_New_data,'ipl_SR_New','SR')



################## sixes  #######################################
mapping_columns(international_data,'international_four','four')
mapping_columns(ipl_old_data,'ipl_four_older','4')
mapping_columns(ipl_New_data,'ipl_four_New','4')


################## sixes  #######################################
mapping_columns(international_data,'international_five','five')
mapping_columns(ipl_old_data,'ipl_five_older','5')
mapping_columns(ipl_New_data,'ipl_five_New','5')


################## dream_11_points  #######################################
mapping_columns(international_data,'international_dream_11_points','dream_11_points')
mapping_columns(ipl_old_data,'ipl_dream_11_points_older','dream_11_points')
mapping_columns(ipl_New_data,'ipl_dream_11_points_New','dream_11_points')


################## consistency in performance  #######################################
mapping_columns(international_data,'international_consistency','consistency')
mapping_columns(ipl_old_data,'ipl_consistency_older','consistency')
mapping_columns(ipl_New_data,'ipl_consistency_New','consistency')

data = data.replace(-np.inf, 0)
data = data.replace(-np.nan, 0)


def weightage_international(df):
        
        total = 1
        a = b = c = 0
        if (df['international_Inns'] >= 1):
            a = 0.3 * total
        
        return a

def weightage_old_ipl(df):
        a = b = c = 0
        total = 1
        a = weightage_international(df)
        total = total - a
        
        if (df['ipl_Inns_older'] >= 1):
            b = 0.3 * total
        
        return b

def weightage_New_ipl(df):
        total = 1
        a = b = c = 0
        a = weightage_international(df)
        b = weightage_old_ipl(df)
        total =  total - b - a
        
        if (df['ipl_Inns_New'] >= 1):
            c = total
            
        return c
    
data['dream_11_points_final_points'] =  (data.apply(weightage_international, axis = 1) * data['international_dream_11_points']
                                        + data.apply(weightage_old_ipl, axis = 1) * data['ipl_dream_11_points_older']
                                        + data.apply(weightage_New_ipl, axis = 1) * data['ipl_dream_11_points_New'])


data = data.sort_values(by = 'dream_11_points_final_points',ascending = False)

data[['dream_11_points_final_points','international_consistency','ipl_consistency_older','ipl_consistency_New']] = data[['dream_11_points_final_points','international_consistency','ipl_consistency_older','ipl_consistency_New']].round(decimals=2)

data.to_csv('final_batsman_list.csv',index=False)


