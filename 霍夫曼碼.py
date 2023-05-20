# 演算法分析機測
# 學號 : 10827102 / 10827108 / 10827203
# 姓名 : 沈柏融 / 鄞志良 / 李昶毅
# 中原大學資訊工程系

from operator import attrgetter
from itertools import combinations
from itertools import permutations

class Node():
  def  __init__(self,name=None,value=None):
    self._name=name
    self._value=value
    self._left=None
    self._right=None
    
class Data():
  def  __init__(self,name=None,code=None):
    self.name=name 
    self.code=code
    
class HuffmanTree():
  def __init__(self,char_weights):
    self.a=[Node(part[0],part[1])  for part in char_weights]
    while len(self.a)!=1:
        self.a.sort(key=lambda  node:node._value,reverse=True)
        c=Node(value=(self.a[-1]._value+self.a[-2]._value))
        c._left=self.a.pop(-1)
        c._right=self.a.pop(-1)
        self.a.append(c)
        self.root=self.a[0]
        self.b=list(range(20))       

  def get_code(self,tree,length):
    node=tree
    if (not node):
      return
    elif node._name:
      code = ''
      for i in range(length):
        code += str(self.b[i]) 
      self.huffman_list.append(Data(node._name,code))
      return
  
    self.b[length]=0
    self.get_code(node._left,length+1)
    self.b[length]=1
    self.get_code(node._right,length+1)
    
  def combine(self,temp_list,n):
    temp_list2=[] 
    for c in combinations(temp_list, n):
      temp_list2.append(c)
    return temp_list2

  def change_to_code(self,n):
    re = ''
    for i in range(len(self.per_list[n])):
      for j in range(len(self.huffman_list)):
        if self.huffman_list[j].name == self.per_list[n][i]:
          re += self.huffman_list[j].code
    return re  

  def decode(self,target):
    self.comb_list=[]
    self.per_list=[]
    name_list=[]
    for obj in self.huffman_list:
      name_list.append(obj.name)
    for i in range(len(name_list)):     
      self.comb_list.extend(self.combine(name_list,i+1))
    for i in range(len(self.comb_list)):
      self.per_list.extend(list(permutations(self.comb_list[i],len(self.comb_list[i]))))
    for i in range(len(self.per_list)):
      if self.change_to_code(i) == target:
        return self.per_list[i]
    
  
  def print_all(self,target,test_num):
    self.huffman_list=[]  
      
    self.get_code(self.root,0)
    self.huffman_list.sort(key=attrgetter('name'))
    print('Huffman Codes #', test_num)
    for obj in self.huffman_list: 
      print( obj.name, obj.code )
    ans = self.decode(target)
    if ans == None :
      print("No answer")
    else :
      print('Decode =', end=' ')
      for i in range(len(ans)):
        print(ans[i],end='')  
      
if __name__== '__main__' :
  test_num = 0
  all_right = True 
  while(1) :
    char_weights = []
    test_num += 1
    token_num = input()
    while not token_num.isnumeric() :
      print('try again')
      token_num = input()
    if token_num == 0 :
      break
    for i in range(int(token_num)):
      ch, weights = input().split(" ")
      #temp=[(str(ch),int(weights))]
      char_weights.append((str(ch),int(weights)))
    #print(char_weights)
    #char_weights=[('a',45),('b',13),('c',12),('d',16),('e',9),('f',5)]
    #print(char_weights)
    target = str(input())
    if not target[i].isdecimal() :
        all_right = False
    
    if all_right == True :
      tree=HuffmanTree(char_weights)
      tree.print_all(target,test_num)
    else :
      print('try again')
      