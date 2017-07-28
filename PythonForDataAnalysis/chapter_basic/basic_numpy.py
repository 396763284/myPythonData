# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:26:56 2017

@author: Administrator
"""

import numpy as np

#numpy

#简单创建
def create1():
    data1=[6,7.5,8,0,1]
    arr1=np.array(data1)
#print arr1

#嵌套序列
def create2():
    data2=[[6,7.5,8,0,1],[6,7.5,8,0,1]]
    arr2=np.array(data2)
    print "维度="+str(arr2.ndim),"维度，列数="+str(arr2.shape)

#新建列表
def create3():
    np.zeros(10)
    np.zeros((3,6))
    #创建新数组，只分配空间不填充值
    np.empty((1,2,3))
    np.arange(10)


# ndarray 的数据类型
def create4():
    arr1=np.array([1,2,3],dtype=np.float64)


#数组与标量
def create5():
    arr=np.array([[1,2,3],[3,4,5]])
    arr*arr
    arr*1
    print arr+1
#create5()

#索引 和 切片
def create6():
    arr=np.arange(10)
    print arr[5]
    #从五到8
    print arr[5:8]
    arr[5:8]=12
       #
    print arr[5:8]
create6()


