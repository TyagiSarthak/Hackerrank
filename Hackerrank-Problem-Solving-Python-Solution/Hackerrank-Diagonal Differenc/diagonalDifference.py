#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):#Take the Matrix and its Order.
    Primary=0
    Secondary=0
    for i in range(n):
        for j in range(n):
            if i==j:#Condition for primary diagonal.
                Primary+=arr[i][j]
            if ((i+j)==(n-1)):#Condition for secondary diagonal.
                Secondary+=arr[i][j]
    if (Primary-Secondary>0):
        return Primary-Secondary
    else:
        return -(Primary-Secondary)#For negative answer of difference.
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
