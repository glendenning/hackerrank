#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):

    highscore = scores[0]
    lowscore = scores[0]
    high = 0
    low = 0

    for score in scores:
        if score > highscore:
            high += 1
            highscore = score 
        if score < lowscore:
            low += 1
            lowscore = score 
    
    return [high, low]
        




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
