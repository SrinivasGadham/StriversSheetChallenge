from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    rows=set()
    coloums=set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                rows.add(i)
                coloums.add(j)
    for row in rows:
        for j in range(len(matrix[0])):
            matrix[row][j]=0
    for column in coloums:
        for i in range(len(matrix)):
            matrix[i][column]=0
