# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:24:24 2017

@author: Administrator
"""

#生成数据

import feedparser
import re

#返回一个RSS订阅源的标题和包含单词计数情况的字典
def getwordcounts(url):
    #解析订阅源
    d=feedparser.pares(url)
    wc={}
    for e in d.entries:
        print e


getwordcounts('http://feeds.feedburner.com/37signals/beMH')