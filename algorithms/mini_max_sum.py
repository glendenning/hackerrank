#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

    arr.sort() 
    minimum = sum(arr[:len(arr) - 1])
    maximum = sum(arr[1:])

    print("%i %i" % (minimum, maximum))


if __name__ == '__main__':
    arr = list(map(int, input().split(" ")))

    miniMaxSum(arr)
