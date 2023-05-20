# 演算法分析機測
# 學號 : 10827102 / 10827108 / 10827203
# 姓名 : 沈柏融 / 鄞志良 / 李昶毅
# 中原大學資訊工程系

def lcs(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    res = [['' for i in range(l2+1)] for j in range(l1+1)]
    num = [[0 for i in range(l2+1)] for j in range(l1+1)]
    for i in range(1,l1+1):
        for j in range(1, l2+1):
            if s1[i-1] == s2[j-1]:
                num[i][j] = num[i-1][j-1]+1
                res[i][j] = res[i-1][j-1] + s1[i-1]
            else:
                if num[i-1][j] > num[i][j-1]:
                    num[i][j] = num[i-1][j]
                    res[i][j] = res[i-1][j]
                else:
                    num[i][j] = num[i][j-1]
                    res[i][j] = res[i][j-1]
    return num[-1][-1],res[-1][-1]

if __name__ == '__main__':
    
    
    num_list = [int(i) for i in input().split()]
    a = 1
    while num_list[0] != 0 and num_list[1] != 0 :
    # 字元串1
      if 1 <= num_list[0] <=100 and 1<= num_list[1] <= 100:
        s1 = input().split()
      # 字元串2
        s2 = input().split()
      # 計算最長公共子序列的長度
        if num_list[0]== len(s1) and num_list[1]== len(s2):
          res = lcs(s1, s2)
          print("Case #", a,sep='')
          print("Length of LCS =",res[0])
          print("LCS =",res[1]) 
          a=a+1
        else:
          print("不符合規定請重頭輸入")
          
      else :
        print("不符合規定請重頭輸入")
     
      num_list = [int(i) for i in input().split()]
      
      
    print("bye bye~")