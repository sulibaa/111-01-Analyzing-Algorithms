# 演算法分析機測
# 學號 : 10827102 / 10827108 / 10827203
# 姓名 : 沈柏融 / 鄞志良 / 李昶毅
# 中原大學資訊工程系

from PIL import Image
import random

imageName = input('enter an image file name ：')
puzzle = Image.open( imageName )

pieceList = []
for a in range(1, 10) : # puzzle = 9 * 16, range(1, 10)  ->  1 ~ 9
    for b in range(1, 17) :
        piece = puzzle.crop((120*(b-1), 120*(a-1), 120*b-1, 120*a-1))
        pieceList.append( piece )

for a in range(1, 10) :
    for b in range(1, 17) :
        r = random.randrange( 0, len(pieceList) ) # random.randrange( 0, 100 )  ->  0 ~ 99
        x = 120 * ( b - 1 )
        y = 120 * ( a - 1 )
        piece = pieceList[r]
        puzzle.paste( piece, (x, y) )

        del pieceList[r]

tittle = imageName.split('.')[0] + '_result.bmp'
puzzle.save(tittle)