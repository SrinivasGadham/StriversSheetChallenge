from os import *
from sys import *
from collections import *
from math import *

def helper(s, string, ans, n, visited):
	# if the length of the "string" is "n", a combination
	# is found and it is appended to "ans"
	if len(string) == n:
		ans.append(string)
		return

	# looping through "s"
	for i in range(n):
		# checking if the character is not visited
		if not visited[i]:
			# marking the character as visited and calling
			# the function recursively
			visited[i] = True
			helper(s, string + s[i], ans, n, visited)
			
			# element is unmarked and looking for next combination
			visited[i] = False


def findPermutations(s):
	ans = []
	n = len(s)
	# used to keep track of visited elements
	visited = [False] * n
	helper(s, "", ans, len(s), visited)
	# finally returning all permutations
	return ans