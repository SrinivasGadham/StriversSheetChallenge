from os import *
from sys import *
from collections import *
from math import *


def nextPermutation(permutation, n):
    flag = 0
    for i in range(n-1, 0, -1):
        if permutation[i] > permutation[i-1]:
            flag = 1
            swap_element = i-1
            break
    if flag == 0:
        permutation.sort()
        return permutation
    max_index = swap_element+1
    for i in range(swap_element+1, n):
        if permutation[swap_element] < permutation[i] and permutation[max_index] > permutation[i]:
            max_index = i
    permutation[swap_element], permutation[max_index] = permutation[max_index], permutation[swap_element]
    permutation[swap_element+1:] = sorted(permutation[swap_element+1:])
    return permutation
