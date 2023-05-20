# 演算法分析機測
# 學號 : 10827102 / 10827108 / 10827203
# 姓名 : 沈柏融 / 鄞志良 / 李昶毅
# 中原大學資訊工程系

def dij(start, graph):
    n = len(graph)
    # 初始化各項資料，把costs[start]初始化為0，其他為無窮大
    # 把各個頂點的父結點設定成-1
    costs = [99999 for _ in range(n)]
    costs[start] = 0
    parents = [-1 for _ in range(n)]
    visited = [False for _ in range(n)] # 標記已確定好最短花銷的點
    t = []  # 已經確定好最短花銷的點列表
    while len(t) < n:
        # 從costs裡面找最短花銷(找還沒確定的點的路徑)，標記這個最短邊的頂點，把頂點加入t中
        minCost = 99999
        minNode = None
        for i in range(n):
            if not visited[i] and costs[i] < minCost:
                minCost = costs[i]
                minNode = i
        t.append(minNode)
        visited[minNode] = True

        # 從這個頂點出發，遍歷與它相鄰的頂點的邊，計算最短路徑，更新costs和parents
        for edge in graph[minNode]:
            if not visited[edge[0]] and minCost + edge[1] < costs[edge[0]]:
                costs[edge[0]] = minCost + edge[1]
                parents[edge[0]] = minNode
    return costs, parents




if __name__ == '__main__':
    num_list = [int(i) for i in input().split()]
    a = 0
    while num_list[0] != 0 and num_list[1] != 0 :
        
      dot = input().split()
      
      for q in range(0, num_list[0]):
          if dot[q] >= 'A' and dot[q] <= 'Z' :
             print("try again~~~")
             dot = input().split()
             break
             
      if num_list[0]== len(dot):
        
        a=a+1
      else:
        print("try again~~~")
        
      data = []
      
      for w in range(0, num_list[1]):
        
        linecount = input()
        dot1 = linecount[0]
        dot2 = linecount[2]
        count = 1
        count = linecount[4]
        k = 5
       # int (count)
        while k < len(linecount) :
          
          count = int(count)*10 + int(linecount[k])
         # print(count)
          k = k + 1
        row = []
       # print(count)
        if dot1 == dot[0] : row.append(0) 
        elif dot1 == dot[1] : row.append(1) 
        elif dot1 == dot[2] : row.append(2) 
        elif dot1 == dot[3] : row.append(3) 
        elif dot1 == dot[4] : row.append(4) 
        elif dot1 == dot[5] : row.append(5) 

        if dot2 == dot[0] : row.append(0) 
        elif dot2 == dot[1] : row.append(1) 
        elif dot2 == dot[2] : row.append(2) 
        elif dot2 == dot[3] : row.append(3) 
        elif dot2 == dot[4] : row.append(4) 
        elif dot2 == dot[5] : row.append(5) 
        #int(count)
        #row.append(dot1) 
        #row.append(dot2) 
        row.append(int(count)) 
        #print(row)
        data.append(row)
        
      
        
      n = num_list[0]  
      graph = [[] for _ in range(n)]
      for edge in data:
          graph[edge[0]].append([edge[1], edge[2]])
        #  graph[edge[1]].append([edge[0], edge[2]])
          
          
          
      costs, parents = dij(0, graph)
      
      
      print('Graph#', a)


      for p in range(1, num_list[0]):
       # print()
        print('From',dot[0],'to',dot[p], '=',costs[p])
        
        
     
      print(dot[0],'source node')
      for p in range(1, num_list[0]):
        print(dot[p],'’s',sep='',end='')
        print(' parent node = ',end='') 
        if parents[p] == 0 : print(dot[0])
        elif parents[p] == 1 : print(dot[1])
        elif parents[p] == 2 : print(dot[2])
        elif parents[p] == 3 : print(dot[3])
        elif parents[p] == 4 : print(dot[4])
       # print(parents)
        
      num_list = [int(i) for i in input().split()]
      
      
    print("bye bye~")
        
  
  