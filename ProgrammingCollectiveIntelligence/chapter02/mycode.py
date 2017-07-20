# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 18:37:56 2017

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


#知识点  字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。 dict.items()




#欧几里德
def sim_distance(prefs,person1,person2):  # Get the list of shared_items
  si={}
  for item in prefs[person1]: 
    if item in prefs[person2]: si[item]=1  # if they have no ratings in common, return 0
  if len(si)==0: return 0  # Add up the squares of all the differences
  sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) 
                      for item in prefs[person1] if item in prefs[person2]])
  return 1/(1+sum_of_squares)

# 皮尔逊相关度评价
def sim_pearson(prefs,p1,p2):
  si={}
  for item in prefs[p1]: 
    if item in prefs[p2]: si[item]=1
  if len(si)==0: return 0
  n=len(si)
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])	
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0
  r=num/den
  return r
        


#为评论者打分
def topMatches(prefs,person,n=5,similarity=sim_pearson):

    # 生产一个 参数 和 人名 的列表
    scores=[(similarity(prefs,person,other),other) for other in prefs if other!=person]
    #sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
    scores.sort()
    #reverse() 函数用于反向列表中元素。
    scores.reverse()
   
    print scores[0:n]
    return scores[0:n]

#topMatches(critics,'Lisa Rose',n=5,similarity=sim_pearson)



#推荐物品
#利用所有他人评价值的加权平均，提供建议
def getRecommendations(prefs,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
        if other==person:continue
        sim=similarity(prefs,person,other)
        #print sim,other
    #忽略评价值小于0
        if sim<=0:continue
        for item in prefs[other]:
        #只对自己还未看过的影片评价
            if item not in prefs[person] or prefs[person][item]==0:
                #相似度*评价值
                totals.setdefault(item,0)
                
                totals[item]+=prefs[other][item]*sim
                #相似度之和
                simSums.setdefault(item,0)
                simSums[item]+=sim
        
        rankings=[(total/simSums[item],item) for item ,total in totals.items()]
        rankings.sort()
        rankings.reverse()
        print rankings
        return rankings

getRecommendations(critics,'Toby',similarity=sim_pearson)     
        





















