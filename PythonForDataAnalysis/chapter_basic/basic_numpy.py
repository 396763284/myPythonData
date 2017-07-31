# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:26:56 2017

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import random
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

#索引 和 切片
def create6():
    arr=np.arange(10)
    print arr[5]
    #从五到8
    print arr[5:8]
    arr[5:8]=12
       #
    print arr[5:8]

# 布尔型索引

# 随机生成 数组  np.random.randn(行 ，列)

def create7():
    data=np.random.randn(2,3)
    #print data
    #print data[0,1:]
    
    # 创建8X4 的数组
    arr=np.empty((5,3))
    for i in range(5):
        arr[i]=i
    print arr
    #特定顺序选取子集 负数从后往前显示
    print arr[[0,4]]
    print arr[[-1,-4]]
    
    
    
#数组转置和轴对换
def create8():
    #创建 从0-15 的 3X5 数组
    arr=np.arange(15).reshape((3,5))
    print arr
    #3X5 转换 5X3
    print arr.T
    #计算内积
    print np.dot(arr.T,arr)
    
    #通用函数
    #sqrt平方根,exp指数，square平方,abs绝对值
    print np.sqrt(arr),np.abs(arr)
    


#利用 数组进行数据处理

def function9():
    points=np.arange(-5,5,1)
    #print points
    xs,ys=np.meshgrid(points,points)
    #print ys
    
    z=np.sqrt(xs**2+ys**2)
    #plt.imshow(z,cmap=plt.cm.gray);plt.colorbar


    #条件逻辑
    xarr=np.array([1,2,3,4,5])
    yarr=np.array([6,7,8,9,10])
    cond=np.array([True,False,True,False,True])
    
    result =np.where(cond,xarr,yarr)
    print result
    
    arr=np.random.randn(4,4)
    arr =np.where(arr>0,2,-2)
    print arr
#function9()
    
    
#数学和统计方法
def function10():
    arr=np.arange(15).reshape((3,5))
    
    print arr
    # mean 算术平均值
    print arr.mean()
    # 轴上的统计   二维的只能统计两种
    print arr.sum(0 )
    
    print arr.cumsum(1)
    
    
    
#function10()    
    

#范例 随机漫步

def example():
    position=0
    walk=[position]
    steps=30
    for i in xrange(steps):
        #randint 从给定的上下范围内随机取整数
        #print np.random.randint(0,1),"----",random.randint(0,1)
        step=1 if random.randint(0,1) else -1
        position+=step
        walk.append(position)
    #print walk
    nwalk=5
    nsteps=10
    draws=np.random.randint(0,2,nsteps)
    steps2=np.where(draws>0,0,-1)
    print steps2
    walk2=steps2.cumsum()
    print walk2
    #创建5X10的随机数
    draws=np.random.randint(0,2,size=(nwalk,nsteps))
    print draws

example()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    


