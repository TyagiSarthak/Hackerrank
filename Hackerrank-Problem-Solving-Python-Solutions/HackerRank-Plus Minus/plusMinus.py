#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    T=len(arr)#Total no. of elements in arr.
    P=0#Total positive integer
    N=0#Total negative integer
    Z=0#Total no. of Zeroes
    for i in range(T):
        if arr[i]>0:
            P+=1
        elif arr[i]<0:
            N+=1
        elif arr[i]==0:
            Z+=1
    print(P/T)
    print(N/T)
    print(Z/T)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
