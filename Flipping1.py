# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 17:50:35 2018

@author: susan
"""

#flip curve

import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import glob

def MergeFiles(Path):
# get files for one group into one dataframe
    Files = glob.glob(Path + "/*.csv")
    WholeGroupFile = pd.DataFrame()
    list_ = []
    for file_ in Files:
        df = pd.read_csv(file_,index_col=None, header=0, engine='python')
        list_.append(df)
    WholeGroupFile = pd.concat(list_)
    return WholeGroupFile

Path = 'C:/Users/susan/Documents/Bachelorarbeit/Osnabrück/Erste Versuche in Python/drive-download-20180204T152457Z-001/Data/Grp21/training/pairAB'
    
MergeFiles(Path)
OnePair = MergeFiles(Path)  
        
def Flipping(OnePair):
        
        
        for index, row in OnePair.iterrows():
        
        
            if row['angle'] == 180 and row['clockwise'] == 0:
            
                diffX = (1420 - row['cursor_X'])
                row['flippedX'] = (500 + diffX)
                diffY = (row['cursor_Y'] - 540)
                row['flippedY'] = (540 - diffY)
                OnePair.at[index, 'flippedX'] = row['flippedX']
                OnePair.at[index, 'flippedY'] = row['flippedY']
            
            elif row['angle'] == 180 and row['clockwise'] == 1:      
                diffX = (1420 - row['cursor_X'])
                row['flippedX'] = (500 + diffX)
                row['flippedY'] = row['cursor_Y']
                OnePair.at[index, 'flippedX'] = row['flippedX']
                OnePair.at[index, 'flippedY'] = row['flippedY']
            
            elif row['angle'] == 0 and row['clockwise'] == 0:
             row['flippedX'] = row['cursor_X']
             row['flippedY'] = row['cursor_Y']
             OnePair.at[index, 'flippedX'] = row['flippedX']
             OnePair.at[index, 'flippedY'] = row['flippedY']
            
            elif row['angle'] == 0 and row['clockwise'] == 1:
             row['flippedX'] = row['cursor_X']
             diffY = (row['cursor_Y'] - 540)
             row['flippedY'] = (540 - diffY)
             OnePair.at[index, 'flippedX'] = row['flippedX']
             OnePair.at[index, 'flippedY'] = row['flippedY']
            
            elif row['angle'] == 270 and row['clockwise'] == 1:
            
                diffX = (1000 - row['cursor_X'])
                row['flippedX'] = (500 + diffX)
                diffY = (row['cursor_X'] -960)
                row['flippedY'] = (540 - diffY)
                OnePair.at[index, 'flippedX'] = row['flippedX']
                OnePair.at[index, 'flippedY'] = row['flippedY']
            elif row['angle'] == 270 and row['clockwise'] == 1:
                diffX = (1000 - row['cursor_Y'])
                row['flippedX'] = (500 + diffX)
                diffY = (960 - row['cursor_X'])
                row['flippedY'] = (540 - diffY)
                OnePair.at[index, 'flippedX'] = row['flippedX']
                OnePair.at[index, 'flippedY'] = row['flippedY']
            elif row['angle'] == 90 and row['clockwise'] == 0:
                 diffX = (row['cursor_X'] - 80)
                 row['flippedX'] = (500 + diffX)
                 diffY = (row['cursor_X'] - 960)
                 row['flippedY'] = (540 - diffY)
                 OnePair.at[index, 'flippedX'] = row['flippedX']
                 OnePair.at[index, 'flippedY'] = row['flippedY']
            #             
            elif row['angle'] == 90 and row['clockwise'] == 1:
                 diffX = (row['cursor_X'] - 80)
                 row['flippedX'] = (500 + diffX)
                 diffY = (960 - row['cursor_X'])
                 row['flippedY'] = diffY - 540
                 OnePair.at[index, 'flippedX'] = row['flippedX']
                 OnePair.at[index, 'flippedY'] = row['flippedY']
        
        
        return OnePair    
          
Flipping(OnePair)

red = Flipping(OnePair)
red.to_pickle('C:/Users/susan/Documents/Bachelorarbeit/Osnabrück/Erste Versuche in Python/drive-download-20180204T152457Z-001/Data/flipped.pkl'
)
#print(red[3000:3300])

#
## Get velocity to a certain time point

