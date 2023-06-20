from os import *
from sys import *
from collections import *
from math import *

def getTrappedWater(arr, n) :
	suffix_sum=[-1 for i in range(n)]
	suffix_sum[0]=arr[0]
	s_sum=[-1 for i in range(n)]
	s_sum[n-1]=arr[n-1]
	

	for i in range(1,n):
		suffix_sum[i]=max(suffix_sum[i-1],arr[i])
	for i in range(n-2,-1,-1):
		s_sum[i]=max(s_sum[i+1],arr[i])
	total=0
	for i in range(n):
		total+=min(suffix_sum[i],s_sum[i])-arr[i]
		
	return total

	