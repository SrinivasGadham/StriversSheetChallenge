

def tabulation(arr, n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):     
        for j in range(1, n + 1): 
            not_take = 0 + dp[i - 1][j]

            take = float('-inf')
            
            if i <= j:
                take = arr[i - 1] + dp[i][j - i]
            
            dp[i][j] = max(take,not_take)

    return dp[n][n]

def cutRod(arr, n):
    
    
    

    
    return tabulation(arr,n)