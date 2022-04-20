#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    dict = {}
    for i in range(len(arr)//2):
        bin = int(arr[i][0])
        if bin not in dict:
            dict[bin]=["-"]
        else:
            dict[bin].append("-")
            
    for i in range(len(arr)//2,len(arr)):
        bin = int(arr[i][0])
        if bin not in dict:
            dict[bin]=[arr[i][1]]
        else:
            dict[bin].append(arr[i][1])
    #print(dict)
            
    s = ""
    for i in sorted(dict.keys()):
        s = s+ " ".join(dict[i]) + " "
    print(s)

if __name__ == '__main__':
    f = open("data.txt
    n = int(f.readline())

    arr = []

    for _ in range(n):
        arr.append(f.readline().split())

    countSort(arr)
