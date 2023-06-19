from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit

def findTriplets(arr, n, k):
    
    arr.sort()

    ans = []

 

    # print(arr)

    

    for i in range(n-2):

        x = arr[i]

        i1 = i+1

        j1 = n-1

        s = x+arr[i1]+arr[j1]

 

        if(i>0 and arr[i-1]==arr[i]):

            continue

 

        

        while(i1<j1):

            

            if(s>k):

                s-=arr[j1]

                j1-=1

                s+=arr[j1]

            elif(s<k):

                s-=arr[i1]

                i1+=1

                s+=arr[i1]

            else:

                ans.append([arr[i],arr[i1],arr[j1]])

                x = arr[i1]

                s-=arr[i1]

                while(i1 < n and arr[i1]==x):

                    i1+=1

                if(i1<n):

                    s+=arr[i1]

 

            

    return ans

















# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    K = int(stdin.readline())
    return N, arr,K


tc = int(input())
while tc > 0:
    N, arr,K = takeInput()
    ans = findTriplets(arr, N,K)

    if len(ans) == 0:
        stdout.write("-1\n")

    else:
        for i in ans:
            i.sort()
            stdout.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

    tc -= 1
