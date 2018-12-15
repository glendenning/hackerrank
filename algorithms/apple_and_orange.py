#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):

    num_apples = 0
    for d in apples:
        if s <= (a + d) <= t:
            num_apples += 1
    
    num_oranges = 0
    for d in oranges:
        if s <= (b + d) <= t:
            num_oranges += 1

    print(num_apples)
    print(num_oranges)

if __name__ == '__main__':
    s, t = map(int, input().split())

    a, b = map(int, input().split())

    m, n = map(int, input().split())

    apples = list(map(int, input().split()))

    oranges = list(map(int, input().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
