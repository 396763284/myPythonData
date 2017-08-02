# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 19:05:17 2017

@author: Administrator
"""
import pandas as pd

def get_data(data_file):
    catering_sale=data_file
    data = pd.read_excel(catering_sale)
    print data.describe()
    return data


#数据预处理



#1.数据清洗
#1.1 缺失值处理

#拉格朗日插值



#处理数据
def deal_data():
    data=get_data("catering_sale.xls")
    #输出路径
    outfile='tmp/sales.xls'
    data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None #过滤异常值，将其变为空值
    print data
    
    
    
deal_data()    
    
    
    
    
    
    
    
    
    