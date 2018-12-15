#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def round(number):
    # round a number up to nearest 5
    divisible = False
    newNumber = number
    i = 0
    while not divisible:
      if (newNumber % 5 != 0):
        i += 1
        newNumber += 1
      else:
          divisible = True
    if (i < 3):
        return newNumber 
    else:
        return number

def gradingStudents(grades):
    #
    # Write your code here.
    #
    finalGrades = []
    for grade in grades:
        if grade >= 38:
            finalGrades.append(round(grade))
        else:
            finalGrades.append(grade)
    return finalGrades

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
