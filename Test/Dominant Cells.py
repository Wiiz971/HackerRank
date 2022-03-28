#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    # Write your code here
    dominant = 0
    for i in range (len(grid)):
        for j in range(len(grid[0])):
            a = grid[i][j]
            k=1
            for p in range(max(0,i-1),min(len(grid),i+2)):
                for l in range(max(0,j-1),min(len(grid[0]),j+2)):
                    if (p,l)!=(i,j) and a <= grid[p][l]:
                        k=0
                        break
                if k==0:
                    break
            else:
                dominant+=1
                
    return dominant


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
