# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Wed Jul 18 18:09:38 2018)---
runfile('C:/Users/user/.spyder-py3/temp.py', wdir='C:/Users/user/.spyder-py3')
clear
print ("Hello")

## ---(Thu Jul 19 13:25:56 2018)---
def main():
    print("Hello")
if __name__ == "__main__":
    main()
"""
Spyder Editor

This is a temporary script file.
"""

def main():
    print("Hello")



if __name__ == "__main__":
    main()
import numpy as np

def main():
    rotation = input("Enter the rotation")




if __name__ == "__main__":
    main()
runfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')
tile = [][]
for i in range(dimension):
    print(i)
for i in range(5):
    print(i)
for i in range(dimension):
    for j in range(dimension):
        tile = input()
print("Enter the array")

for i in range(dimension):
    for j in range(dimension):
        tile = input()
def main():
    rotation = input("Rotation - ")
    dimension = input("Dimension - ")
    
    tile = [][]
    
    print("Enter the array")
    
    for i in range(dimension):
        for j in range(dimension):
            tile = input()
import numpy as np

def main():
    rotation = input("Rotation - ")
    dimension = input("Dimension - ")
    
    tile = [[]]
    
    print("Enter the array")
    
    for i in range(dimension):
        for j in range(dimension):
            tile = input()
runfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')
tile = []
for i in range(4):
    tile[i] = list(input().split())


print(tile)
runfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')

## ---(Thu Jul 19 14:53:23 2018)---
print("Enter the array")

tile = [[]]
for i in range(4):
    tile[i] = list(input().split())


print(tile)
print("Enter the array")

tile = []
for i in range(4):
    tile.append([])
    for j in range(4):
        tile[0] = input().split()
print("Enter the array")

tile = []
for i in range(4):
    tile.append([])
    for j in range(4):
        tile[0] = list(input().split())


print(tile)
tile = []

for i in range(4):
    tile.append([])


for i in range(4):
    tile[0] = list(input().split())


print(tile)
clear
print("Enter the array")

tile = []

for i in range(4):
    tile.append([])


for i in range(4):
    tile[0] = list(input().split(" "))


print(tile)
print("Enter the array")

tile = []

for i in range(4):
    tile.append([])


for i in range(4):
    tile[i] = list(input().split(" "))


print(tile)
print(tile,"\n",tile)
for i in range(4*2):
    print(i)
for i in range(dimension*2):
    tess.append([])
tess= "\"
print(tess)
tess= "\\"
print(tess)

## ---(Thu Jul 19 17:36:40 2018)---
runfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')
tile
tess
rotate90
print(tile)
tile
runfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')
tess
tessellation
tess
clear
tess = []
tess
def main():
    rotation = int(input("Rotation - "))
    dimension = int(input("Dimension - "))
    
    tessellation(rotation,dimension)
def tessellation(rotation, dimension):
    print("Enter the array")
    
    for i in range(dimension):
        tile.append([])
    
    for i in range(dimension):
        tile[i] = list(input().split(" "))
    
    if rotation == 90:
        tess = rotate90()
 #   elif rotation == 180:
 #       new_tile = rotate180()
  #  elif rotation == 270:
   #     new_tile = rotate270()
    
    print(tess)
rotation = 0
dimension = 0

tile = []
def main():
    rotation = int(input("Rotation - "))
    dimension = int(input("Dimension - "))
    
    tessellation(rotation,dimension)
print("Enter the array")

for i in range(dimension):
    tile.append([])


for i in range(dimension):
    tile[i] = list(input().split(" "))
"""

rotation = 0
dimension = 0

tile = []

def rotate90():
    tess = []
    tile_row = 0
    tile_column = 0
    for i in range(dimension*2):
        tess.append([])
    for i in range(dimension*2):
        for j in range(dimension*2):
            
            if(tile[tile_row][tile_column] == "*"):
                tile[tile_row][tile_column] = "*"
                tess[i][j] = "*"              
            elif(tile[tile_row][tile_column] == "/"):
                tile[tile_row][tile_column] = "\\"
                tess[i][j]= "\\"              
            elif(tile[tile_row][tile_column] == "\\"):
                tile[tile_row][tile_column] = "//"
                tess[i][j] = "/"              
            elif(tile[tile_row][tile_column] == '#'):
                tile[tile_row][tile_column] = "#"
                tess[i][j] = "#"               
            elif(tile[tile_row][tile_column] == "-"):
                tile[tile_row][tile_column] = "|"
                tess[i][j] = "|"               
            elif(tile[tile_row][tile_column] == "|"):
                tile[tile_row][tile_column] = "-"
                tess[i][j] = "-"             
            elif(tile[tile_row][tile_column] == "+"):
                tile[tile_row][tile_column] = "+"
                tess[i][j] = "+"               
            elif(tile[tile_row][tile_column] == "."):
                tile[tile_row][tile_column] = "."
                tess[i][j] = "."
            
            tile_column = tile_column + 1
            
            if (tile_column == 3):
                tile_column = 0
        
        tile_row = tile_row + 1
        if(tile_row == 3):
            tile_row = 0
    print (tile)


#def rotate180():

#def rotate270():


def tessellation(rotation, dimension):
    print("Enter the array")
    
    for i in range(dimension):
        tile.append([])
    
    for i in range(dimension):
        tile[i] = list(input().split(" "))
    
    if rotation == 90:
        tess = rotate90()
 #   elif rotation == 180:
 #       new_tile = rotate180()
  #  elif rotation == 270:
   #     new_tile = rotate270()
    
    print(tess)


def main():
    rotation = int(input("Rotation - "))
    dimension = int(input("Dimension - "))
    
    tessellation(rotation,dimension)



if __name__ == "__main__":
    main()
runfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')
if rotation == 90:
    tess = rotate90()
tile[tile_row][tile_column] = "*"
runfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')
array = np.asarray(tile)
array
runfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')
debugfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')
clear
debugfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')
tile[0][0] = "*"
t_array = np.asarray(tile)
t_array = np.array(tile)
debugfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')

## ---(Thu Jul 19 19:46:15 2018)---
t_array = np.zeros
import numpy as np

t_array = np.zeros
debugfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')
t_array = np.array(tile
t_array = np.array(tile)
debugfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')

## ---(Thu Jul 19 21:19:16 2018)---
debugfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')
runfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')
clear
runfile('C:/Users/user/.spyder-py3/tessellation.py', wdir='C:/Users/user/.spyder-py3')