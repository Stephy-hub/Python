# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
#import os
#import fnmatch
import numpy as np
import glob


#directory = r'C:\Users\stephy.wilson\Documents\Python Scripts\testData'


#all_data = pd.DataFrame()
for f in glob.glob(r'C:\Users\stephy.wilson\Documents\Python Scripts\testData\*.xlsx'):
    df = pd.read_excel(f)
    df1 = df['x']
    #all_data = all_data.append(df,ignore_index=True)
    

#for path,dirs,files in os.walk(directory):
 #   for file in files:
  #      if fnmatch.fnmatch(file,'*.xlsx'):
   #         fullname = os.path.join(path,file)
    #        print(fullname) 
           
            
    
#df = pd.read_excel(r'C:\Users\stephy.wilson\Documents\Python Scripts\testData\xy_testData1.xlsx')

#plt.plot(df.x, df.y)
#print (df)
#for filename in os.listdir(directory):
 #   if filename.endswith(".xlsx"):
  #      df = pd.read_excel(directory, filename.endswith(".xlsx"))
   #     
        
    #else:
     #   continue