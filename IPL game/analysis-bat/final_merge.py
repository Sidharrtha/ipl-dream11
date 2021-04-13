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
mapping_columns(international_data,'international_Runs','Runs')
mapping_columns(ipl_old_data,'ipl_Runs_older','Runs')
mapping_columns(ipl_New_data,'ipl_Runs_New','Runs')

################## highest score #######################################
mapping_columns(international_data,'international_HS','HS')
mapping_columns(ipl_old_data,'ipl_HS_older','HS')
mapping_columns(ipl_New_data,'ipl_HS_New','HS')


################## Batting average #######################################
mapping_columns(international_data,'international_Ave','Ave')
mapping_columns(ipl_old_data,'ipl_Ave_older','Ave')
mapping_columns(ipl_New_data,'ipl_Ave_New','Ave')

################## Balls face #######################################
mapping_columns(international_data,'international_BF','BF')
mapping_columns(ipl_old_data,'ipl_BF_older','BF')
mapping_columns(ipl_New_data,'ipl_BF_New','BF')

################## Strike Rate #######################################
mapping_columns(international_data,'international_SR','SR')
mapping_columns(ipl_old_data,'ipl_SR_older','SR')
mapping_columns(ipl_New_data,'ipl_SR_New','SR')


################## Century  #######################################
mapping_columns(international_data,'international_Century','hundred')
mapping_columns(ipl_old_data,'ipl_Century_older',100)
mapping_columns(ipl_New_data,'ipl_Century_New',100)



################## fifty  #######################################
mapping_columns(international_data,'international_fifty','fifties')
mapping_columns(ipl_old_data,'ipl_fifty_older',50)
mapping_columns(ipl_New_data,'ipl_fifty_New',50)



################## ducks  #######################################
mapping_columns(international_data,'international_ducks','duck')
mapping_columns(ipl_old_data,'ipl_ducks_older',0)
mapping_columns(ipl_New_data,'ipl_ducks_New',0)


################## fours  #######################################
mapping_columns(international_data,'international_fours','fours')
mapping_columns(ipl_old_data,'ipl_fours_older','4s')
mapping_columns(ipl_New_data,'ipl_fours_New','4s')



################## sixes  #######################################
mapping_columns(international_data,'international_sixes','sixes')
mapping_columns(ipl_old_data,'ipl_sixes_older','6s')
mapping_columns(ipl_New_data,'ipl_sixes_New','6s')


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
    
data['dream_11_points_final_points'] =  (data.apply(weightage_international, axis = 1) * data['international_consistency']
                                        + data.apply(weightage_old_ipl, axis = 1) * data['ipl_consistency_older']
                                        + data.apply(weightage_New_ipl, axis = 1) * data['ipl_consistency_New'])


data = data.sort_values(by = 'dream_11_points_final_points',ascending = False)

data[['dream_11_points_final_points','international_consistency','ipl_consistency_older','ipl_consistency_New']] = data[['dream_11_points_final_points','international_consistency','ipl_consistency_older','ipl_consistency_New']].round(decimals=2)

data.to_csv('final_batsman_list.csv',index=False)


