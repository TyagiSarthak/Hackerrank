#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1,n+1):
        print(str("#"*i).rjust(n))#The string rjust() method returns a new string of given length after 
                                 #substituting a given character in left side of original string.

if __name__ == '__main__':
    n = int(input())

    staircase(n)
