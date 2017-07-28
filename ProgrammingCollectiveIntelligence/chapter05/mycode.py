97# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 17:53:47 2017

@author: Administrator
"""
# Python
#  strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
#  time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。
#   range（start， end， scan): 计数
#优化
import time
import random
import math

people = [('Seymour','BOS'),
          ('Franny','DAL'),
          ('Zooey','CAK'),
          ('Walt','MIA'),
          ('Buddy','ORD'),
          ('Les','OMA')]


destination='LGA'

flights={}

for line in file('schedule.txt'):
   
    origin,dest,depart,arrive,price=line.strip().split(',')
    #确定出发地  终点 航班
    flights.setdefault((origin,dest),[])
    #添加航班详情
    flights[(origin,dest)].append((depart,arrive,int(price)))
#print flights
  
# 给定时间 在一天中的分钟数
def getminutes(t):
    x=time.strptime(t,'%H:%M')
    #x[] 0 year ,1 tm_mon ,3 tm_hour=11,4 tm_min=22,
    return x[3]*60+x[4]
  
#getminutes('11:22')

# 描述题解
s=[1,4,3,1,7,3,6,3,2,4,5,3]
def printshedule(r):
    for d in range(len(r)/2):
        name=people[d][0]
        origin=people[d][1]
        
        out=flights[(origin,destination)][int(r[d])]
        ret=flights[(destination,origin)][int(r[d+1])]
        print '%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name,origin,
                                                  out[0],out[1],out[2],
                                                 ret[0],ret[1],ret[2])


#printshedule(s)
  
#成本函数
def schedulecost(sol):
    totalprice=0
    latestarrival=0
    earliestdep=24*60
    for d in range(len(sol)/2):
        #得到往返航班 
        origin=people[d][1]
        outbount=flights[(origin,destination)][int(sol[2*d])]
        returnf=flights[(origin,destination)][int(sol[2*d+1])]
        
        # 总价格 所有往返价格之和
        totalprice+=outbount[2]
        totalprice+=returnf[2]
        #记录最晚到达时间和最早离开时间
        if latestarrival<getminutes(outbount[1]):latestarrival=getminutes(outbount[1])
        if earliestdep>getminutes(returnf[0]):earliestdep=getminutes(returnf[0])
    # 每个人必须在机场等待知道最后一个人到达为止
    totalwait=0
    for d in range(len(sol)/2):
        origin=people[d][1]
        outbount=flights[(origin,destination)][int(sol[2*d])]
        returnf=flights[(origin,destination)][int(sol[2*d+1])]
        totalwait+=latestarrival-getminutes(outbount[1])
        totalwait+=getminutes(returnf[0])-earliestdep
        
    if latestarrival<earliestdep:totalwait+50
    #print totalprice+totalwait
    return totalprice+totalwait
        
        
#schedulecost(s)
  

#随机搜索

#domain 指定变量的最大最小值
#成本 函数
def randomoptimize(domain,costf):
    best=9999999
    bestr=None
    #随机产生1000次猜测
    for i in range(0,10):
        #创建一个随机解 
        #从0-9 中随机生产一个数字，加到
        #domain[i][0]=0,domain[i][1]=9
        r=[float(random.randint(domain[i][0],domain[i][1])) 
            for i in range(len(domain))]
        #得到成本
        print r
        cost=costf(r)
        
        #与目前为止的最优解进行比较
        if cost<best:
            best=cost
            bestr=r
    return r


# 执行方法
# 生产  人数2倍 的 (0,9) 

domain=[(0,9)]*(len(people)*2)


#s=randomoptimize(domain,schedulecost)

#schedulecost(s)
#print schedulecost(s)


# 爬山法

def hillclimb(domain,schedulecost):
    sol=[float(random.randint(domain[i][0],domain[i][1])) 
            for i in range(len(domain))]
    #主循环
    while 1:
        #创建相邻解的列表
        neighbors=[]
        for j in range(len(domain)):
            #在每个方向上相对于 原值 偏离一点
            if sol[j]>domain[j][0]:
                neighbors.append(sol[0:j]+[sol[j]-1]+sol[j+1:])
            if sol[j]<domain[j][0]:
                neighbors.append(sol[0:j]+[sol[j]+1]+sol[j+1:])
        # 在相邻解中寻找最优解
        current=costf(sol)
        best=current
        for j in range(len(neighbors)):
            cost=costf(neighbors[j])
            if cost<best:
                best=cost
                sol=neighbors[j]
        if best==current:
                break
        return sol
                



hillclimb(domain,schedulecost)
  
  
  
  
  