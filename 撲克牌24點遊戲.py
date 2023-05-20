# 演算法分析機測
# 學號 : 10827102 / 10827108 / 10827203
# 姓名 : 沈柏融 / 鄞志良 / 李昶毅
# 中原大學資訊工程系

def generate_comb_op(n):
      # 找出所有的符號排列
      if n==0:
          return [] # 當n為0時不返回任何操作符號
      elif n ==1:
          return [['+'],['-'],['*'],['/']] 
      op_list = generate_comb_op(n-1) 
      # 新建一個list用遞回的方式將原先的list加入新符號
      all_op_list = [] 
      # 最後我們還是要用迴圈的邏輯來給我們原來list裡的元素加新的符號
      for i in op_list:
          for j in ['+','-','*','/']:
              all_op_list.append(i+[j]) # 這裡用了新的list，來確保每個sublist的長度是相等的
  
      return all_op_list # 最後返回最終結果
  
  
def generate_permutated_list(num_list):
      # 找出所有的數字排列
      if len(num_list) == 0:
          return [] # 當n為0時不返回任何數字
      if len(num_list) == 1:
          return [num_list] # 當n為1時返回所有式子，作為之後首數字的基礎
      list_of_comb = [] # 新建列表來存更新的排列
      for i in range(len(num_list)):
          first_num = num_list[i] # 生成首字母
          for j in generate_permutated_list(num_list[:i] + num_list[i+1:]): # 去除首字母，繼續遞迴
              list_of_comb.append([first_num] + j) #加入新的list
  
      return list_of_comb # 最後返回最終結果
  
  
  #################################### 定義所有可能出現的數學操作，包括加減乘除 ####################################
  
def division(a,b): # 除法比較特殊，用了try except來考慮到被除數為0的情況
      try:
          return a/b
      except:
          return ''
  
def multiply(a,b):
      return a*b
def add(a,b):
      return a+b
def subtract(a,b):
      return a-b
  
  ############################################ 數學表示式處理函式 ##############################################
  
def modify_op(equation, op):

      # 這裡我們把代表數學計算的字串和以上定義的操作函式的名字以字典的方式聯絡並儲存起來
      operators = {'/':division, '*':multiply, '+':add, '-':subtract}
      
      while op in equation: # 用while迴圈來確保沒有遺漏任何字元
          i = equation.index(op) # 找到表示式內的第一處需要計算的字元位置
          # 把表示式需要計算的部分替換成計算結果
          if equation[i+1] != '' and equation[i-1] != '':
              equation[i-1:i+2] = [str(operators[op](float(equation[i-1]), float(equation[i+1])))] # 注意這裡呼叫了前面字典裡儲存的函式名
          else:
              return ['']
      return equation # 返回結果
  
def evaluate(equation):
     for i in range(len(equation)):
      if type(equation[i]) == list: # 如果表示式型別為list
              equation[i] = evaluate(equation[i]) # 滿足括號條件，開始遞迴
     for op in ['/','*','+','-']:
          equation = modify_op(equation, op) # 使用helper function
  
     return equation[0] # 最後返回最終計算結果
  ############################################# 括號位置生成函式 #############################################
  
def layer_sort(equation, depth=3): # 預設湊對的長度為3（這裡是因為兩個數字加一個運算子號有三位數）
      if depth == len(equation): # 如果湊對長度達到表示式總長，便返回表示式原式
          return []
      layer_comb = [] # 初始化一個總列表
  
      # 我們要從最左邊開始定義左括號的位置，然後在相應長度的結束定義右括號的位置
      # len(equation)-depth+1 為最右邊的左括號合理位置+1，是迴圈的結束位置
      for i in range(0,len(equation)-depth+1,2): # 間隔為2，因為我們要跳過一個數字和一個符號
          new_equation = equation[:i]+[equation[i:i+depth]]+equation[i+depth:] # 寫出新表示式
          layer_comb.append(new_equation)
      for j in layer_sort(equation, depth+2):
         layer_comb.append(j)
      return layer_comb
 
def generate_all_brackets(equation):
 
     layer_possibility = layer_sort(equation) # 找到本層可用的表示式
     all_possibility = layer_possibility[:]
     for i in layer_possibility:
         if len(i) > 3: # 檢查是否達成遞迴條件，這一步同時也是這個遞迴函式的base case
             next_layer_equ = generate_all_brackets(i)
             for j in next_layer_equ: # 去重操作
                 if j not in all_possibility:
                     all_possibility.append(j)
 
     return [equation] + all_possibility # 不要忘了在列表最開始加入原式
 
 ########################################### 字串格式轉換函式 #############################################
 
def convert_to_str(equation_list):
     equation = '' # 初始化字串表示式
     for i in range(len(equation_list)):
         if type(equation_list[i]) == list: # 這裡是遞迴條件，如果資料型別為list，我們要把括號內的表示式傳到下一層
             equation += '(' + convert_to_str(equation_list[i]) + ')' # 加入括號
         else:
             equation += equation_list[i] # base case， 如果資料型別不是list，那麼就普通返回字串
     return equation # 返回字串形式的表示式
 
 ############################################# 最終使用函式 ################################################
 
def get_card(num_list):
     op_list = generate_comb_op(len(num_list) - 1)  # 找出所有加減乘除的排列組合
     num_comb = generate_permutated_list(num_list)  # 找出所有數字的排列組合
     # 用for巢狀迴圈來整合所有表示式可能
     for each_op_list in op_list:
         for each_num_list in num_comb:
             equation, equation_list= [], []  # 初始化基礎表示式，以及基礎+括號表示式
             for i in range(len(each_op_list)):
                 equation.extend([str(each_num_list[i]), each_op_list[i]])
             equation.append(str(each_num_list[-1])) # 組裝基礎表示式
             equation_list.append(equation) # 把基礎表示式加入基礎+括號表示式的列表
             equation_list.extend(generate_all_brackets(equation)) # 把所有括號表示式加入括號表示式的列表
             for each_equation in equation_list:
                 equation_str = convert_to_str(each_equation) # 先把列表轉化成字串
                 if evaluate(each_equation) == str(float(24)): # 如果最終結果相等便返回字串
                     return equation_str
               
############################################# 主函式 ################################################                    
               
def main():             
    if __name__ == '__main__':
        main()
        
num_list = [int(i) for i in input().split()]
while num_list[0] != 0 :
    re = str(get_card(num_list))
    if re == "None" :
        print("No Solution")
    else :
        print(re)
    num_list = [int(i) for i in input().split()]
        
print("bye bye~")