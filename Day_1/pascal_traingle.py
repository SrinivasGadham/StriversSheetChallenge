# from os import *
# from sys import *
# from collections import *
# from math import *

def printPascal(n:int):
    rows=n
    columns=n
    matrix=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        matrix[0][i]=1
    for i in range(n):
        matrix[i][0]=1
    for i in range(1,n):
        for j in range(1,n):
            matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
    # print(matrix)
    res=[]
    for i in range(rows):
        row = i
        col = 0
        l=[]
        while row>=0 and col<=i:
            l.append(matrix[row][col])
            row-=1
            col+=1
        res.append(l)
    return res
    

    
