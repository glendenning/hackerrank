#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):

    # measure the initial gap of kangaroos
    kangaroo1 = x1
    kangaroo2 = x2

    # move the kangaroos to their next jump
    while kangaroo1 != kangaroo2:

        gapBefore = abs(kangaroo1 - kangaroo2)
        kangaroo1 += v1
        kangaroo2 += v2 
        gapAfter = abs(kangaroo1 - kangaroo2)

        if (gapAfter >= gapBefore):
            # The gap got bigger after a jump
            return "NO"
        elif (kangaroo1 == kangaroo2):
            # keep jumping them
            return "YES"
        else:
            continue


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1, v1, x2, v2 = map(int, input().split())

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
