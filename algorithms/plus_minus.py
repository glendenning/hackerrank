#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

    pos = 0
    neg = 0
    zero = 0

    for item in arr:
        if item > 0:
            pos += 1
        elif item < 0:
            neg += 1
        elif item == 0:
            zero += 1
    
    print("%.6f" % (pos / len(arr)))
    print("%.6f" % (neg / len(arr)))
    print("%.6f" % (zero / len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
