# 演算法分析機測
# 學號 : 10827102 / 10827108 / 10827203
# 姓名 : 沈柏融 / 鄞志良 / 李昶毅
# 中原大學資訊工程系

num = int()
order = []
order_temp = []
data = []
open_door = False

def samenum( num ) :
    same = False
    for l in range(len(order_temp)) :
        if num == order_temp[l] :
            same = True
    if same :
        return True
    else :
        return False
    

def sort( order_temp ) :
    i = 0
    global order
    global open_door 
    
    while i < num :
        #input("press enter")
        if not samenum( i ) :
            #print(data[i][0])
            #print(data[order_temp[len(order_temp)-1]][len(data[order_temp[len(order_temp)-1]])-1])
           # input("press enter")
            if data[i][0] == data[order_temp[len(order_temp)-1]][len(data[order_temp[len(order_temp)-1]])-1] :
                order_temp.append( i )
                #input("press enter")
                if len(order_temp) == num :
                    open_door = True
                    order = order_temp
                else :
                    sort( order_temp )
        i = i + 1
        #print(i," ",num)
        

token = str()
door_num = 1
num = int(input())
while num != 0 :
    open_door = False
    data.clear()
    
    for i in range( num ) :
        token = str(input())
        data.append(token)
    
    j = 0
    while not open_door and j < num :
        order.clear()
        order_temp.clear()
        
        order_temp.append( j )
        sort( order_temp )
        j = j + 1
    
    if open_door :
        print("Secret Door1", door_num)
        print( "Can be open" )
        door_num = door_num + 1
        
        for i in range(len(order)) :
            print(data[order[i]], end = '')
            if i != len(order)-1 :
                print("-", end = '')
    else :
        print("Secret Door1", door_num)
        print( "Can not be open" )
            
    num = int(input())
        

print("bye bye~")