from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n):
    count = 0

    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort(left_half)
            merge_sort(right_half)

            merge(arr, left_half, right_half)

    def merge(arr, left_half, right_half):
        nonlocal count
        i = j = k = 0
        left_len = len(left_half)
        right_len = len(right_half)

        while i < left_len and j < right_len:
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
                count += left_len - i  # Increment count by the remaining elements in the left half
            k += 1

        while i < left_len:
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < right_len:
            arr[k] = right_half[j]
            j += 1
            k += 1

    merge_sort(arr)
    return count

def takeInput():
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

arr, n = takeInput()
print(getInversions(arr, n))
