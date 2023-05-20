# 演算法分析機測
# 學號 : 10827102 / 10827108 / 10827203
# 姓名 : 沈柏融 / 鄞志良 / 李昶毅
# 中原大學資訊工程系

class Data :
    def __init__(self, W_wolf, W_sheep, boat_position, E_wolf, E_sheep) :
        
        self.W_wolf  = W_wolf
        self.W_sheep = W_sheep
        self.boat_position  = boat_position 
        self.E_wolf  = E_wolf
        self.E_sheep = E_sheep

    def print_data( self ) :  # ( W_wolf W_sheep )(boat_position)( E_wolf E_sheep )
        print( "( " + str(self.W_wolf) + " " + str(self.W_sheep) + " ) ", end = '' )
        print( "( " + self.boat_position + " ) ", end = '' + "\n" )
        #print( "( " + str(self.E_wolf) + " " + str(self.E_sheep) + " ) " + "\n" )

    def safe( self ) :
        if self.W_wolf > self.W_sheep and self.W_sheep != 0 :
            return False
        elif self.E_wolf > self.E_sheep and self.E_sheep != 0 :
            return False
        else :
            return True
        
    def same_data( self, data ) :
        if self.W_wolf == data.W_wolf and self.W_sheep == data.W_sheep and self.boat_position == data.boat_position and self.E_wolf == data.E_wolf and self.E_sheep == data.E_sheep :           
            return True
        else :
            return False    
    

class Comb :

    def __init__(self, W_wolf, W_sheep, boat_position, E_wolf, E_sheep) :
        self.Data = Data( W_wolf, W_sheep, boat_position, E_wolf, E_sheep )
        self.Data_list = [ self.Data ]
        self.Data_all = [self.Data_list]
        self.Purpose = Data( 0, 0, "E", W_wolf, W_sheep )
        
    def find_same_data( self, nowData ) :
        for Data in self.Data_list :
            if Data.same_data( nowData ) :
                return True

        return False

    '''def print_all( self ) :
        shortest = int(len( self.Data_all[0] ))
        shortest_num = 0
        for i in len(self.Data_all) :
            if len( self.Data_all[0] ) < shortest :
                shortest_num = i
        for Data in self.Data_all[shortest_num] :
            Data.print_data()'''
            
    def print_all( self ) :
        for Data in self.Data_list :
            Data.print_data()

    def cross_river( self, nowData ) :
        # 已全部移至東邊 結束
        if nowData.same_data( self.Purpose ) :
            self.Data_all.append( self.Data_list )
            return True

        # W to E
        if nowData.boat_position == "W" :
            try_times = 0
            
            # 西向東移 2狼
            if nowData.W_wolf >= 2 : 
                next_data = Data( nowData.W_wolf - 2, nowData.W_sheep, "E", nowData.E_wolf + 2, nowData.E_sheep )
                if next_data.safe() and not Comb.find_same_data( self, next_data ) :
                    try_times += 1
                    self.Data_list.append( next_data )
                    if Comb.cross_river( self, next_data ) :
                        return True
                    
            # 西向東移 2羊
            if nowData.W_sheep >= 2 :
                next_data = Data( nowData.W_wolf, nowData.W_sheep - 2, "E", nowData.E_wolf, nowData.E_sheep + 2 )
                if next_data.safe() and not Comb.find_same_data( self, next_data ) :
                    try_times += 1
                    self.Data_list.append( next_data )
                    if Comb.cross_river( self, next_data ) :
                        return True
                    
            # 西向東移 1狼 1羊         
            if nowData.W_wolf >= 1 and nowData.W_sheep >= 1 : 
                next_data = Data( nowData.W_wolf - 1, nowData.W_sheep - 1, "E", nowData.E_wolf + 1, nowData.E_sheep + 1 )
                if next_data.safe() and not Comb.find_same_data( self, next_data ) :
                    try_times += 1
                    self.Data_list.append( next_data )
                    if Comb.cross_river( self, next_data ) :
                        return True
                    
            # 西向東移 1狼
            if nowData.W_wolf >= 1 :
                next_data = Data( nowData.W_wolf - 1, nowData.W_sheep, "E", nowData.E_wolf + 1, nowData.E_sheep )
                if next_data.safe() and not Comb.find_same_data( self, next_data ) :
                    try_times += 1
                    self.Data_list.append( next_data )
                    if Comb.cross_river( self, next_data ) :
                        return True      
                    
            # 西向東移 1羊
            if nowData.W_sheep >= 1 :
                next_data = Data( nowData.W_wolf, nowData.W_sheep - 1, "E", nowData.E_wolf, nowData.E_sheep + 1 )
                if next_data.safe() and not Comb.find_same_data( self, next_data ) :
                    try_times += 1
                    self.Data_list.append( next_data )
                    if Comb.cross_river( self, next_data ) :
                        return True
                    
            # 無解 返回上層遞迴
            if try_times == 0 :
                self.Data_list.pop()

        # E to W
        if nowData.boat_position == "E" :
            try_times = 0

            # 東向西移 2狼
            if nowData.E_wolf >= 2 : 
                next_data = Data( nowData.W_wolf + 2, nowData.W_sheep, "W", nowData.E_wolf - 2, nowData.E_sheep )
                if next_data.safe() and not Comb.find_same_data( self, next_data ) :
                    try_times += 1
                    self.Data_list.append( next_data )
                    if Comb.cross_river( self, next_data ) :
                        return True
                    
            # 東向西移 2羊
            if nowData.E_sheep >= 2 :
                next_data = Data( nowData.W_wolf, nowData.W_sheep + 2, "W", nowData.E_wolf, nowData.E_sheep - 2 )
                if next_data.safe() and not Comb.find_same_data( self, next_data ) :
                    try_times += 1
                    self.Data_list.append( next_data )
                    if Comb.cross_river( self, next_data ) :
                        return True
                    
            # 東向西移 1狼 1羊
            if nowData.E_wolf >= 1 and nowData.E_sheep >= 1 :
                next_data = Data( nowData.W_wolf + 1, nowData.W_sheep + 1, "W", nowData.E_wolf - 1, nowData.E_sheep - 1 )
                if next_data.safe() and not Comb.find_same_data( self, next_data ) :
                    try_times += 1
                    self.Data_list.append( next_data )
                    if Comb.cross_river( self, next_data ) :
                        return True
                    
            # 東向西移 1狼
            if nowData.E_wolf >= 1 :
                next_data = Data( nowData.W_wolf + 1, nowData.W_sheep, "W", nowData.E_wolf - 1, nowData.E_sheep )
                if next_data.safe() and not Comb.find_same_data( self, next_data ) :
                    try_times += 1
                    self.Data_list.append( next_data )
                    if Comb.cross_river( self, next_data ) :
                        return True 
                    
            # 東向西移 1羊
            if nowData.E_sheep >= 1 :
                next_data = Data( nowData.W_wolf, nowData.W_sheep + 1, "W", nowData.E_wolf, nowData.E_sheep - 1 )
                if next_data.safe() and not Comb.find_same_data( self, next_data ) :
                    try_times += 1
                    self.Data_list.append( next_data )
                    if Comb.cross_river( self, next_data ) :
                        return True
                    
            # 無解 返回上層遞迴
            if try_times == 0 :
               
                self.Data_list.pop()



def main():             
    if __name__ == '__main__':
        main()

while ( 1 ) : 
    total_wolf, total_sheep = map( int, input().split() )

    if total_wolf == 0 and total_sheep == 0 :
        break

    generate = Comb( total_wolf, total_sheep, "W", 0, 0 ) # ( W_wolf, W_sheep, boat_position, E_wolf, E_sheep )
    if generate.cross_river( generate.Data ) :
        generate.print_all()
    else :
        print("No answer!")
        
print("bye bye~")