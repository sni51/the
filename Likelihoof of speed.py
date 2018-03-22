# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:10:25 2018

@author: susan
"""

# Likelihood of speed

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

red = pd.read_pickle('C:/Users/susan/Documents/Bachelorarbeit/Osnabrück/Erste Versuche in Python/drive-download-20180204T152457Z-001/Data/flipped.pkl')

red['SquSpeedX'] = red['speedX']**2
red['SquSpeedY'] = red['speedY']**2


red['Velocity'] = np.sqrt(red[['SquSpeedX','SquSpeedY']].sum(axis=1))

parts = [0,1,2,3,4] #why do I need to put 5 in here to get a legend for part 4?
                    #when I try to plot all of them in one graph
for part in parts:
    
    Slice = red[red['part'] == part]
    Velocity = Slice['Velocity']
    
    fig = plt.figure()
    plt.title('Part_'+ str(parts[part]))
    plt.xlabel('Velocity')
    plt.ylabel('Frequency')
    plt.ylim(0,1600)
    plt.xlim(0,3.5)
    #if I get 5 different plots I don't get a label. Why?
    plt.hist(Velocity, histtype = 'bar', label= parts)
           

 


