"""Today we'll your challenge is to write a program that can do basic regular tessellations in ASCII art.

Input Description
    You'll be given an integer on the first line, which can be positive or negative.
    It tells you the rotation (relative to clockwise, so 180, 90, 0, or -90) to spin the tile as you tessellate it.
    The next line contains a single integer that tells your program how many columns and rows to read (assume it's a square).
    Then the next N rows contain the pattern of the tile in ASCII art.

Example:

90
4
# # # #
# - - #
# + + #
# # # #


Output Description

Your program should emit a tessellation of the tile, with the rotation rules applied,
repeated at least two times in both the horizontal and vertical directions, you can do more if you wish.
For the above:

########
#--##+|#
#++##+|#
########
########
#+|##++#
#+|##--#
########"""

def rotate():
    global tile
    if rotate == 90:
        for i in range(dimension):
            for j in range(dimension):
                if tile[i][j] == '#':
                    tile[i][j] = '#'
                elif tile[i][j] == '-':
                    tile[i][j] = '|'
                elif tile[i][j] == '|':
                    tile[i][j] = '-'
                elif tile[i][j] == '*':
                    tile[i][j] = '*'
                elif tile[i][j] == '+':
                    tile[i][j] = '+'
                elif tile[i][j] == '\\':
                    tile[i][j] = '/'
                elif tile[i][j] == '/':
                    tile[i][j] = '\\'
                elif tile[i][j] == '>':
                    tile[i][j] = 'v'
                elif tile[i][j] == 'v':
                    tile[i][j] = '<'
                elif tile[i][j] == '<':
                    tile[i][j] = '^'
                elif tile[i][j] == '^':
                    tile[i][j] = '>'
                elif tile[i][j] == '.':
                    tile[i][j] = '.'