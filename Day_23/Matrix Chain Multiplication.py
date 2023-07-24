def matrixMultiplication(arr, n):
	
	
	def tabulation():
		dp = [ [0]*n for _ in range(n) ]

		for i in range(n-1,0,-1):
			for j in range(i+1,n,1):
				mini = float('inf')

				for k in range(i,j):
					steps = arr[i-1]*arr[k]*arr[j] + dp[i][k] + dp[k+1][j] 

					if steps < mini :
						mini = steps

				dp[i][j] = mini

		return dp[i][j]
	
	
	
	

	
	return tabulation()