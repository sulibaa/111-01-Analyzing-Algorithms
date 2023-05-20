# 演算法分析機測
# 學號 : 10827102 / 10827108 / 10827203
# 姓名 : 沈柏融 / 鄞志良 / 李昶毅
# 中原大學資訊工程系

import sys
from itertools import combinations

def combine(temp_list,n):
    temp_list2=[] 
    for c in combinations(temp_list, n):
      temp_list2.append(c)
    return temp_list2

while 1 :
  v = int(input()) #背包體積
  if v == 0:
    break
  elif v < 0 :
    print( 'wromg input' )
    sys.exit(0)
  n = int(input()) #物品數量
  if n < 0 :
    print( 'wromg input' )
    sys.exit(0)
  
  
  success = False  
  while not success :
    all_bigger_than_bag = True
    goods = [] # 初始化
    for i in range(n):
      goods.append(list(map(int, input().split()))) 
      if int(goods[i][0]) <= v :
        all_bigger_than_bag = False
    
      if int(goods[i][0]) < 0 :
        print('try again')
        break
      elif int(goods[i][1]) < 0 : 
        print('try again')
        break
      success = True

  if all_bigger_than_bag :
    print('no answer')
  else :

    # 計算
    dp = [[0 for i in range(v + 1)] for j in range(n + 1)] # 初始化
    for i in range(1, n + 1):
      for j in range(1, v + 1):
        dp[i][j] = dp[i - 1][j] # 不裝
        if j >= goods[i - 1][0]:
    # 如果還有空間
          dp[i][j] = max(dp[i][j], dp[i - 1][j - goods[i - 1][0]] +
          goods[i - 1][1]) # 對比裝跟不裝
    """ # 输出最优值矩阵 for i in dp: print(i) """
    # 计算最优解


    temp_list = [i for i in range(1,n+1)]
    comb_list = []
    for i in range(1,n+1) :
      comb_list.extend(combine(temp_list,i)) 
  
    for i in range(len(comb_list)):
      x = [0 for k in range(1,n + 2)] # 初始化0：不装，1：装
      value = 0
      for j in range(len(comb_list[i])):
        value = value + int(goods[comb_list[i][j]-1][1])
        x[comb_list[i][j]] = 1
      if value == dp[-1][-1] :
        break
    
    # 输出+++++++++++++++++++++

    print('Total Value =', dp[-1][-1])
    print('\nItems',end='')

    first_num = True ;
    for i in range(0, n+1):
      if first_num == True & x[i] == 1 :
        first_num = False
        print(str(i), end='')
      elif x[i] == 1 :
        print( ',',str(i), end='')
    
    # 输出

print('done')