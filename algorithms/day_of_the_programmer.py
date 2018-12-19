#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):

    isLeapYear = False
    if (1700 <= year <= 1917) and (year % 4 == 0):
        # is a leap year in Julian calendar
        isLeapYear = True
    if (1919 <= year <= 2700) and ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
        # is a leap year in the Gregorian calendar
        isLeapYear = True
    
    # if it's a leap year the 256th day is the 13.09.year
    # if it's not a leap year the 256th day is the 12.09.year

    if (year == 1918):
        return "26.09." + str(year)
    elif (isLeapYear):
        return "12.09." + str(year) 
    else:
        return "13.09." + str(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
