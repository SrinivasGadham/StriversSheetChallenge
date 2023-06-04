from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def sort012(arr, n):
    temp = []
    d = Counter(arr)
    # print(d)
    for i in range(3):
        while d[i]:
            # print(i)
            temp.append(i)
            d[i] -= 1
    # print(temp)
    for i in range(len(temp)):
        arr[i] = temp[i]

        # write your code here
    # don't return anything
    # pass


# taking inpit using fast I/O
def takeInput():
    n = int(input().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


def printAnswer(arr, n):

    for i in range(n):

        print(arr[i], end=" ")

    print()

# main


t = int(input().strip())
for i in range(t):

    arr, n = takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
