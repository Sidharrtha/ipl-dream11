# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 09:26:53 2021

@author: Rajat.Dhawale
"""


import pandas as pd


df1 = pd.read_csv('IPL Ball-by-Ball 2008-2020.csv')

df2 = pd.read_csv('IPL Matches 2008-2020_2.csv') 

data = pd.DataFrame()

data = df1.copy()

gk = data.groupby(['id','inning','batsman']).first().reset_index()

pk = data.groupby(['id','inning','batsman']).agg({'batsman_runs':'sum'}).reset_index()

gk['batsman_runs'] = pk['batsman_runs']


gk.drop(['over','ball','non_striker','bowler','extra_runs','total_runs','non_boundary'],
  axis='columns', inplace=True)
# data['batsman_runs'] = data['batsman_runs']

# gk['extras_type'] = gk['extras_type'].fillna(0)
pk = data[data['batsman_runs']==0].groupby(['id','inning','batsman']).count().reset_index()
for index , row in  pk.iterrows():
              index = gk.index[(gk['id'] == row['id'])
                            & (gk['inning'] == row['inning'])
                            & (gk['batsman'] == row['batsman'])]
                            # & (gk['extras_type'] == 0)]
              print(index)
              gk.loc[index,"0s"] = row['batsman_runs']
              
# pk = data[data['extras_type']=='legbyes'].groupby(['id','inning','batsman']).count().reset_index()
# for index , row in  pk.iterrows():
#               index = gk.index[(gk['id'] == row['id'])
#                             & (gk['inning'] == row['inning'])
#                             & (gk['batsman'] == row['batsman'])
#                             & (gk['extras_type'] == 'legbyes')]
#               print(index)
#               gk.loc[index,"0s"] = row['batsman_runs']
    
pk = data[data['batsman_runs']==1].groupby(['id','inning','batsman']).count().reset_index()
for index , row in  pk.iterrows():
              index = gk.index[(gk['id'] == row['id'])
                            & (gk['inning'] == row['inning'])
                            & (gk['batsman'] == row['batsman'])]
                            # & (data['batsman_runs'].astype(str) == (vouchername))]
              print(index)
              gk.loc[index,"1s"] = row['batsman_runs']

pk = data[data['batsman_runs']==2].groupby(['id','inning','batsman']).count().reset_index()
for index , row in  pk.iterrows():
              index = gk.index[(gk['id'] == row['id'])
                            & (gk['inning'] == row['inning'])
                            & (gk['batsman'] == row['batsman'])]
                            # & (data['batsman_runs'].astype(str) == (vouchername))]
              print(index)
              gk.loc[index,"2s"] = row['batsman_runs']

pk = data[data['batsman_runs']==3].groupby(['id','inning','batsman']).count().reset_index()
for index , row in  pk.iterrows():
              index = gk.index[(gk['id'] == row['id'])
                            & (gk['inning'] == row['inning'])
                            & (gk['batsman'] == row['batsman'])]
                            # & (data['batsman_runs'].astype(str) == (vouchername))]
              print(index)
              gk.loc[index,"3s"] = row['batsman_runs']
              
pk = data[data['batsman_runs']==4].groupby(['id','inning','batsman']).count().reset_index()
for index , row in  pk.iterrows():
              index = gk.index[(gk['id'] == row['id'])
                            & (gk['inning'] == row['inning'])
                            & (gk['batsman'] == row['batsman'])]
                            # & (data['batsman_runs'].astype(str) == (vouchername))]
              print(index)
              gk.loc[index,"4s"] = row['batsman_runs']


pk = data[data['batsman_runs']==6].groupby(['id','inning','batsman']).count().reset_index()

for index , row in  pk.iterrows():
              index = gk.index[(gk['id'] == row['id'])
                            & (gk['inning'] == row['inning'])
                            & (gk['batsman'] == row['batsman'])]
                            # & (data['batsman_runs'].astype(str) == (vouchername))]
              print(index)
              gk.loc[index,"6s"] = row['batsman_runs']

# gk['6s'] = pk['over']




gk['total_runs'] = gk['batsman_runs']

gk = gk.fillna(0)

gk['total_ball_faces'] = gk['0s']+gk['1s']+gk['2s']+gk['3s']+gk['4s']+gk['6s']
gk['strike_rate'] = (gk['total_runs']/gk['total_ball_faces'])*100


gk['dream11_points'] = (gk['1s']+gk['2s']*2+gk['3s']*3+gk['4s']*4+gk['6s']*6)*1+gk['4s']*1+gk['6s']*2

gk['dream11_points'] = gk['dream11_points'] + [16 if x >= 100 else 8 if   x >= 50 else 4 if x >= 30 else 0  for x in gk['total_runs']]

for index , row in  df2.iterrows():
              index = gk.index[(gk['id'] == row['id'])]
                            # & (data['batsman_runs'].astype(str) == (vouchername))]
              print(index)
              gk.loc[index,"date"] = row['date']
              gk.loc[index,'year/season'] = row['date'].split('/')[2]
# gk['year/season'] = gk['date'].split('/')[2]

pk = gk.groupby(['id','inning','batsman','year/season']).first().reset_index()

pk = pk[pk['year/season']=='2008']
pk = pk["batsman"].value_counts().to_dict()
pk = pd.DataFrame.from_dict(pk,orient='index')
pk.reset_index(inplace=True)
pk = pk.rename(columns={'index':'batsman',0:'Mat'})
# mydict = dict(zip(pk.batsman, ck.batsman))
# ck = pk[pk['year/season']=='2008']
for index , row in  pk.iterrows():
              # if gk['year/season'] == 
              index = gk.index[(gk['batsman'] == row['batsman'])]
                            # & (data['batsman_runs'].astype(str) == (vouchername))]
              print(index)
              gk.loc[index,"date"] = row['date']
              gk.loc[index,'year/season'] = row['date'].split('/')[2]
#


