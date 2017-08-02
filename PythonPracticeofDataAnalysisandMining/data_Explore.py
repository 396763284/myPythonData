# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 10:37:22 2017

@author: Administrator
"""
import pandas as pd
import matplotlib.pyplot as plt

#数据探索

#第一节  ：数据质量分析

#缺失值 
#异常值 -箱型图
#不一致的值
#重复数据及含有特殊符号的 数据

#平均值mean 标准差 std 最小值 min 最大值 max 以及分位数1/4,1/2,3/4
def get_data():
    catering_sale='catering_sale.xls'
    data = pd.read_excel(catering_sale, index_col = u'日期')
    print data.describe()

    return data

#异常值检测
def box_check(fuc):
    data =fuc()
    #创建图像
    plt.rcParams['font.sans-serif']=['SimHei']#正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
    plt.figure(figsize=(8,26)) #建立图像
    #创建箱型图
    #The kind of object to return. The default is axes ‘axes’ returns the matplotlib axes the boxplot is drawn on; ‘dict’ returns a dictionary whose values are the matplotlib Lines of the boxplot; 
    #‘both’ returns a namedtuple with the axes and dict.
    p = data.boxplot(return_type='dict') #画箱线图，直接使用DataFrame的方法
    x=p['fliers'][0].get_xdata()# 'flies'即为异常值的标签
    y=p['fliers'][0].get_ydata()
    y.sort() #从小到大排序，该方法直接改变原对象
    #添加注释并处理注释重叠
    for i in range(len(x)): 
        if i>0:
            plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.05 -0.8/(y[i]-y[i-1]),y[i]))
        else:
            plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.08,y[i]))

    plt.show() #展示箱线图
    
#box_check(get_data)



#第二节 ：数据特征分析

#1.分布分析
# 定量分析

#求级差 ；分组：极差/组距；分点：按组距分 ；频率分布


#定性分析
#每一类型的百分比或频数


#2.对比分析



#3 统计量 分析
#集中趋势度量

def statistics(fuc):
     data =fuc()
     statistics=data.describe()
     #极差= 最大值-最小值
     statistics.loc['range']=statistics.loc['max']-statistics.loc['min']
     #变异系数 = 标准差/均值
     statistics.loc['var']=statistics.loc['std']/statistics.loc['min']
     #四分位数间距 值越大，变异程序越大
     statistics.loc['dis']=statistics.loc['75%']-statistics.loc['25%']

     print statistics


#周期性分析
# 随时间变化得出的变化趋势

    

#贡献度分析

def contribution():
     catering_sale='catering_dish_profit.xls'
     data = pd.read_excel(catering_sale, index_col = u'菜品名')
     data=data[u'盈利'].copy()
     plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
     plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
     plt.figure()
     # 柱状图显示
     data.plot(kind='bar')
     #最左侧显示
     plt.ylabel(u'盈利（元）')
     #data.cumsum() 累计 求和
     p = 1.0*data.cumsum()/data.sum()
     p.plot(color = 'r', secondary_y = True, style = '-o',linewidth = 2)
     plt.annotate(format(p[6], '.4%'), xy = (6, p[6]), xytext=(6*0.9, p[6]*0.9), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")) #添加注释，即85%处的标记。这里包括了指定箭头样式。
     #最右侧显示
     plt.ylabel(u'盈利（比例）')
     plt.show()
#contribution()


#相关性分析

#相关系数  Pearson系数  spearman系数  判定系数
def correlation():
     catering_sale='catering_sale_all.xls'
     data = pd.read_excel(catering_sale, index_col = u'日期')
     print data.corr()

     data.corr()#相关系数矩阵 任意两款菜系之间的相关系数
     data.corr()[u'百合酱蒸凤爪']
     data[u'翡翠蒸香茜饺'].corr()[u'百合酱蒸凤爪']


correlation()

