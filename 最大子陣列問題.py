# 演算法分析機測
# 學號 : 10827102 / 10827108 / 10827203
# 姓名 : 沈柏融 / 鄞志良 / 李昶毅
# 中原大學資訊工程系

n = int(input())
while n != 0 :
    A = [int(i) for i in input().split()]
    if len(A) > n :
        print( "more than ",n," numbers !plese try again!" )
    if len(A) < n :
        print( "less than ",n," numbers !plese try again!" )
    else :
        sum = -65535
        temp = 0
        count = 0 # 計數器，用於計算low & high
        lock = False # 找到low並開始找high 除非有新的low
        low = 0 ;
        high = 0 ;
        for i in A :
            count += 1
            temp += i
            if temp > 0 :
                if not lock :
                    low = count
                    lock = True
            if sum < temp :
                sum = temp
                high = count
            if temp <= 0 :
                temp = 0
                lock = False
                
        print("Low=",low,",High=",high,"Sum=",sum )
        
    n = int(input())
    
print("bye bye~")