# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:47:38 2020

@author: dell
"""


import numpy as np
import os
import pandas as pd
#载入数据
#path=os.path.abspath('..')
#path1=path+'\\data\\bankChurn.csv'
#bankData=pd.read_csv(path1,encoding='utf-8')
#bankData.head()

def dataPlot(data,col1,col2):  
    cdata=data[[col1,col2]]
    Grouped1=cdata.groupby([col1,col2])[col1].count()/cdata.groupby([col1])[col1].count()
#print(Grouped1)
    unGrouped1=Grouped1.unstack()
    name=unGrouped1.index.tolist()
    Grouped3=cdata.groupby(col2)[col2].count()/len(cdata)
# TGI
    TGI=(unGrouped1[1]/Grouped3.loc[1])*100
    x1=cdata.groupby(col1)[col1].count()*100/len(cdata)
    name1=[]
    for i in range(len(TGI.values)):
        n=name[i]
        d=TGI.values
        if not np.isnan(d[i]):
            name1.append(n)    
    TGI1=[]
    for i in TGI.values:
        if not np.isnan(i):
            TGI1.append(int(i))
    x=[]
    for i in range(len(TGI.values)):
        d=TGI.values
        val=x1.values[i]
        if not np.isnan(d[i]):
            x.append(val)
    return ({'name':name1,'TGI':TGI1,'x1':x})
    
