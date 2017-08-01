# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 16:41:40 2017

@author: Administrator
"""

#pandas 入门
from  pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#基础数据结构
#series  带索引的数组 索引从0到N-1

def function1():
    obj=Series([1,7,-5,3])
    print obj.values ,obj.index
    obj2=Series([1,7,-5,3],index=['a','b','c','d'])
    print obj2
    #索引查看
    print obj2['a']
    #通过字典 创建
    sdata={'ahio':10,'b':20}
    obj3=Series(sdata)
    print obj3
    states=['ahio','b','a']
    obj4=Series(sdata,index=states)
    print obj4
    # isnull  notnull
    print pd.isnull(obj4)
    print obj3+obj4
    obj4.name='population'
    obj4.index.name='state'
    print obj4
 
#function1()

#DataFrame 表格型数据结构 类似值为数组的 json  {'a':[]}
def function2():
    data={'state':['a','b','c','d','e'],
            'year':[2015,2016,2017,2018,2019],
            'pop':[1.1,1.2,1.3,1.4,1.5]}
    frame=DataFrame(data)
    print frame
    #索引
    print frame['pop']




# 基本功能 series DataFrame
#算术运算和数据对齐
def function3():
     obj1=Series([1,7,-5,3],index=['a','b','c','d'])
     #重置索引  插值处理
     obj2=obj1.reindex(['b','c','d','r','a'],fill_value=0)
    
     print obj1+obj2
     
     #带重复值的轴索引
     
     
     # 创建 dataframe
     print np.arange(12).reshape((4,3))
     df1=DataFrame(np.arange(12).reshape((4,3)),columns=list('bcd'),index=['a','b','c','d']) 
     print df1
     df2=DataFrame(np.arange(20).reshape((4,5)),columns=list('abcde'),index=['a','b','c','d']) 

     print df1.add(df2,fill_value=0)


#汇总和计算描述统计

def function3():
    df=DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],index=['a','b','c','d'],columns=['one','two'])
    #汇总统计
    print df.describe()
    
    # data.iteritems(): 迭代字典
    #相关系数和协方差
    
    #处理缺失数据
    
    string_data=Series(['aa','bb','cc',np.nan])
    # 返回仅含非空数据
    print string_data.dropna()
   #dataframe  dropna 丢弃任何含有缺失值
    cleaned =df.dropna()
    print cleaned
    #dropna 丢弃全为nan
    cleaned1 =df.dropna(how='all')
    
    df1=DataFrame(np.random.randn(7,3))
    df1.ix[2:,1]=np.nan;df1.ix[4:,2]=np.nan
    #Keep only the rows with at least 2 non-na values:
    print df1
    print df1.dropna(thresh=3)
    
    #填充缺少数据
    
    #df1.fillna(0)
    print df1.fillna(method='ffill')
    
    
function3()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


