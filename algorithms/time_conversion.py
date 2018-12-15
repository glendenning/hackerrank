#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # 07:05:45PM
    # 0123456789
    hh = int(s[0:2])
    period = s[8:len(s)]
    print("period " + period)
    if (hh <= 11 and period == 'PM'):
        hh += 12
    elif (hh == 12 and period == 'AM'):
        hh = 0
    
    military_time = str(hh).zfill(2) + ":" + s[3:7+1]
    
    return military_time

    
    


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
