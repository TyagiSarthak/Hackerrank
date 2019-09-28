#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()#this will sort the list arr in ascending order.
    Min=sum(arr)-arr[4]#this will give mini sum.
    Max=sum(arr)-arr[0]#this will give max sum.
    print(Min,Max,end="")#this will print min and max sum separated by space.

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
