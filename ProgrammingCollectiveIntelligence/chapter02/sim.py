# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:46:23 2017

@author: Administrator
"""

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

from math import sqrt

#python知识点
#len(arry[]) 数组长度
# pow(a,2) 求a的平方
# sum([item for item in a if item in b])
# item for item in a if item in b 列表推导式简洁写法

#prefs 数据源 person 列名
def sim_dsitance_my(prefs,person1,person2):
    #
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
            print si
    #
    if len(si)==0: return 0
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2] ])
    print sum_of_squares
    return 1/(sqrt(sum_of_squares)+1)
            

    
sim_dsitance_my(critics,'Lisa Rose','Gene Seymour')    
    

a=[1,2,3,4,5]
b=[2,6,7,8,9]
c=sum([pow(item,2) for item in a if item in b])
print c
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    