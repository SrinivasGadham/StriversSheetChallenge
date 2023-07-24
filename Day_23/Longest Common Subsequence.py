
from sys import stdin

def lcs(text1, text2) :
	def tabulation(n,m):
		dp = [ [-1]*(m+1) for _ in range(n+1) ]
		
		
		for j in range(m+1):
			dp[0][j] = 0
		for i in range(n+1):
			dp[i][0] = 0
		
		for i in range(1,n+1):
			for j in range(1,m+1):
					if text1[i-1]==text2[j-1]:
						dp[i][j] = 1 + dp[i-1][j-1]
					else:
						dp[i][j] = max(dp[i-1][j], dp[i][j-1])
					
		return dp[n][m]

	
	n,m = len(text1),len(text2)

	
	
	

	
	return tabulation(n,m)






























    



s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))