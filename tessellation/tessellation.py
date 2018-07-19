# -*- coding: utf-8 -*-
"""
filename - tessellation.py
author - MyMindPalace

Description
    A Tessellation (or Tiling) is the act of covering a surface with a pattern of flat shapes so that there are no overlaps or gaps.
    Tessellations express fascinating geometric and symmetric properties as art,
    and famously appear in Islamic art with four, five, and six-fold regular tessellations.
    
    
Input
tessellation dimension - 2
tile dimension - 4
# # # #
# - - #
# + + #
# # # #

Output
# # # # # # # #
# - - # # - - #
# + + # # + + #
# # # # # # # # 
# # # # # # # #
# - - # # - - #
# + + # # + + #
# # # # # # # # 

"""

tessellation_dimension = 0
tile_dimension = 0
tile = []
tess = []




    
    
def tessellation():
    global tile,tessellation_dimension,tile_dimension
    tile_row = 0
    tile_column = 0
    print("Enter the array")

    for i in range(tile_dimension):
        tile.append([])

    for i in range(tile_dimension):
        tile[i] = list(input().split(" "))
    
    for i in range(tile_dimension*tessellation_dimension):
        tess.append([])
        
    for i in range(tile_dimension*tessellation_dimension):
        for j in range(tile_dimension*tessellation_dimension):
            tess[i].append(tile[tile_row][tile_column])
            tile_column = tile_column + 1
            if tile_column == tile_dimension:
                tile_column = 0
        tile_row = tile_row + 1
        if tile_row == tile_dimension:
            tile_row = 0
    
    for i in range(tile_dimension*tessellation_dimension):
        print(tess[i])
            

    
def main():
    global tile_dimension,tessellation_dimension
    tessellation_dimension = int(input("Tessellation Dimension - "))
    tile_dimension = int(input("Tile Dimension - "))
    
    tessellation()

        
if __name__ == "__main__":
    main()
    
