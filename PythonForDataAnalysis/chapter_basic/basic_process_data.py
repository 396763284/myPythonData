# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 18:30:50 2017

@author: Administrator
"""
import numpy as np
import pandas as pd
from  pandas import Series,DataFrame
#数据规整

#合并数据集
def function1():
    #pandas.merge
    
    df1=DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
    df2=DataFrame({'key':['a','b','d'],'data2':range(3)})

    print df1 
    print df2
    # how='left'  左连接
    print pd.merge(df1,df2,on='key')

function1()