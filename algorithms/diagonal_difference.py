#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    left = 0
    right = 0
    for i, row in enumerate(arr):
        left += row[i]
        right += row[n-i-1]
    difference = abs(left - right)
    return difference

if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split(" "))))

    result = diagonalDifference(arr)

    print(result)
