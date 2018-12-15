#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):

    birds = list(set(arr))

    birdCount = [0] * len(birds)

    for birdId in arr:
        # Find the index it is in birds
        # add it to bird count
        index = birds.index(birdId)
        birdCount[index] += 1

    highestBirdId = birds[0]
    highestBirdCount = birdCount[0]
    for birdId, birdCount in zip(birds, birdCount):
        # Find the highest frequency bird
        if (birdCount > highestBirdCount) or (birdCount == highestBirdCount and birdId < highestBirdId):
            highestBirdId = birdId 
            highestBirdCount = birdCount 
    
    return highestBirdId


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
