
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    min = 0
    max = 0
    arr.sort()
    n = len(arr)

    j = n-1
    # Write your code here
    for a in range(0, n-1):
        print(arr[a])
        min = min + arr[a]

        max = max + arr[j]
        j -= 1
    print(min, max)


if __name__ == '__main__':

    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)
