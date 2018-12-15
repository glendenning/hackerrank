#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(arr):

    highest = max(arr)
    candles = 0
    for item in arr:
        if item == highest:
            candles += 1
    
    return candles

if __name__ == '__main__':

    ar_count = int(input())

    arr = list(map(int, input().split(" ")))

    result = birthdayCakeCandles(arr)

    print(result)
