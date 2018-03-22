# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 23:11:01 2018

@author: susan
"""

#Slicing

import pandas as pd
import scipy



import random
import math
import numpy as np


#df=pd.read_csv('distance1.csv', sep=',',header=0)
#
#points = np.array(df)
#
#x = points[:,1]
#y = points[:,2]
#
#
#z = np.polynomial.polynomial.polyfit(x,y,[101, 154, 364, 417])
#f = np.poly1d(z)
#print(f)
















#distance = [0]
##print(len(distance))
#
#for i in range(0,517):
#    
#    x2 = df['0'][i+1]
#    x1 = df['0'][i]
#    y2 = df['1'][i+1]
#    y1 = df['1'][i]
#    
#    
#    dist = np.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
#    
#    distance.append(dist)
#
#df['distance'] = distance
#
#
#for j in range(0,517):
#    
#    df['distance'][j+1] = df['distance'][j] + df['distance'][j+1]
#
#    
#while df['distance'] < 10:
#    df['bin'] == 0
#    print(df)

#df.to_pickle('C:/Users/susan/Documents/Bachelorarbeit/Osnabrück/Erste Versuche in Python/drive-download-20180204T152457Z-001/Data/distance.pkl')

distance = pd.read_pickle('C:/Users/susan/Documents/Bachelorarbeit/Osnabrück/Erste Versuche in Python/drive-download-20180204T152457Z-001/Data/distance.pkl')

binn = []

distance['bin'] = binn

distance[distance['bin']==0] = distance.loc[(distance['distance']>10),'distance']
#b = distance.query('10 < distance < 20')
#w = distance['distance'] <= 10 
    
print(distance)
