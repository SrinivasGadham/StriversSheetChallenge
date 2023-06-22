import math
import statistics

def getMedian(matrix):
    l=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            l.append(matrix[i][j])
    l.sort()
    return statistics.median(l)

    