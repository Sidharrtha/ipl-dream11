# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:19:36 2021

@author: Rajat.Dhawale
"""


import pandas as pd


df1 = pd.read_excel('season_2008-2019.xlsx',sheet_name='Bat')

df1['total_boundy'] = df1['6s'] + df1['4s']
df1.sort_values(by=['total_boundy'], inplace=True, ascending=False)
