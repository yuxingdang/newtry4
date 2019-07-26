# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 16:20:41 2018

@author:职问
"""
#时间序列-数据操作与绘图

#知识点1：数据库导入
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#知识点2：数据导入
ibm_stock = pd.read_csv ('ibmclose.txt')


#知识点3：可视化应用
x_time = ibm_stock['Time']
y_price = ibm_stock['Price']

plt.figure()

plt.plot(x_time,y_price)
plt.title('IBM Stock Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

#知识点4：随机数调整
np.random.seed(0)

random_data = np.random.randn(len(x_time))
print(random_data)

len(random_data)

plt.figure()

plt.plot(x_time,y_price+(random_data*10))
plt.title('IBM Stock Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')


#知识点5：数据处理
drinks = pd.read_csv('drinks.csv')

drinks.info()
#运行后结果如下：
#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 193 entries, 0 to 192
#Data columns (total 6 columns):
#country                         193 non-null object
#beer_servings                   193 non-null int64
#spirit_servings                 193 non-null int64
#wine_servings                   193 non-null int64
#total_litres_of_pure_alcohol    193 non-null float64
#continent                       170 non-null object
#dtypes: float64(1), int64(3), object(2)
#memory usage: 9.1+ KB

print(drinks.describe())
#运行后结果如下，可以看到四个int和float类型数据的列，
#所对应的常见统计信息（计数、平均值、标准差、最小值、百分位数、最大值等）：
# beer_servings  spirit_servings  wine_servings  \
#count     193.000000       193.000000     193.000000   
#mean      106.160622        80.994819      49.450777   
#std       101.143103        88.284312      79.697598   
#min         0.000000         0.000000       0.000000   
#25%        20.000000         4.000000       1.000000   
#50%        76.000000        56.000000       8.000000   
#75%       188.000000       128.000000      59.000000   
#max       376.000000       438.000000     370.000000   

#       total_litres_of_pure_alcohol  
#count                    193.000000  
#mean                       4.717098  
#std                        3.773298  
#min                        0.000000  
#25%                        1.300000  
#50%                        4.200000  
#75%                        7.200000  
#max                       14.400000  


# 提取出啤酒这一列的数据作为数据系列
beer_series = drinks['beer_servings']
# 仅统计啤酒服务这一列
print(drinks['beer_servings'].describe())
#或者也可以：
print(beer_series.describe())
#运行后，得到下面的结果：
#count    193.000000
#mean     106.160622
#std      101.143103
#min        0.000000
#25%       20.000000
#50%       76.000000
#75%      188.000000
#max      376.000000
#Name: beer_servings, dtype: float64


print(beer_series.mean())
#得到的结果是106.16062176165804，跟上面使用.describe得到的结果是一样的。

#有条件的查询
euro_frame = drinks[drinks['continent'] == 'EU']
print(euro_frame)


#复合条件的查询
euro_wine_300_frame = drinks[(drinks['continent'] =='EU') & 
                             (drinks['wine_servings'] > 300)]
print(euro_wine_300_frame)
#运行后结果如下：
#      country  beer_servings  spirit_servings  wine_servings  \
#3     Andorra            245              138            312   
#61     France            127              151            370   
#136  Portugal            194               67            339   

#     total_litres_of_pure_alcohol continent  
#3                            12.4        EU  
#61                           11.8        EU  
#136                          11.0        EU  

#排序函数
top_ten_countries = drinks.sort_values (by='total_litres_of_pure_alcohol').tail(10)
print(top_ten_countries)


#我们可以使用ibmclose rank.txt这个文件来作为排序示例：
test = pd.read_csv('ibmclose rank.txt')

print(test)
#运行结果如下：
#   Time  Price
#0     1    460
#1     2    457
#2     7    463
#3     3    479
#4     4    493
#5    12    490
#6    11    492
#7    10    498
#8    13    499

#假设希望根据Time重新排序，那么可以使用下面的语句：
rank1 = test.sort_values(by='Time')

print(rank1)
#运行结果如下，是按照升序排列：
#   Time  Price
#0     1    460
#1     2    457
#3     3    479
#4     4    493
#2     7    463
#7    10    498
#6    11    492
#5    12    490
#8    13    499


#假设希望根据Price重新排序，那么可以使用下面的语句：
rank2 = test.sort_values(by='Price')

print(rank2)
#运行结果如下，是按照升序排列：
#   Time  Price
#1     2    457
#0     1    460
#2     7    463
#3     3    479
#5    12    490
#6    11    492
#4     4    493
#7    10    498
#8    13    499


#假设，我们希望在价格的基础上，进一步只返回数值最大/最小的3组数据，
#那么可以使用tail()/head()：
rank2_max = test.sort_values(by='Price').tail(3)
print(rank2_max)
#运行结果如下，因为数据是升序排列，所以tail就是找到了尾部最后3个数据，实际上就是最大值：
#   Time  Price
#4     4    493
#7    10    498
#8    13    499

rank2_min = test.sort_values(by='Price').head(3)
print(rank2_min)
#运行结果如下，因为数据是升序排列，所以tail就是找到了尾部最后3个数据，实际上就是最大值：
#   Time  Price
#1     2    457
#0     1    460
#2     7    463

#5）缺失数据值补充
drinks['continent'].fillna(value='NA')

drinks.info()

#如果希望在原DataFrame中修改，则把inplace设置为True
drinks['continent'].fillna(value='NA', inplace=True)

#6）插入数据列
drinks['total_servings'] = drinks.beer_servings +drinks.spirit_servings + drinks.wine_servings
drinks['alcohol_mL'] = drinks.total_litres_of_pure_alcohol * 1000

#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 193 entries, 0 to 192
#Data columns (total 8 columns):
#country                         193 non-null object
#beer_servings                   193 non-null int64
#spirit_servings                 193 non-null int64
#wine_servings                   193 non-null int64
#total_litres_of_pure_alcohol    193 non-null float64
#continent                       193 non-null object
#total_servings                  193 non-null int64
#alcohol_mL                      193 non-null float64
#dtypes: float64(2), int64(4), object(2)
#memory usage: 12.1+ KB

#7）可视化绘图
#建立空白图
plt.figure()
#绘制散点图
plt.scatter(drinks['total_litres_of_pure_alcohol'],drinks['beer_servings'])

#坐标轴命名
plt.xlabel('Total Litres of Alcohol')
plt.ylabel('Beer Servings')
#图形命名
plt.title('International Alcohol Statistics')







