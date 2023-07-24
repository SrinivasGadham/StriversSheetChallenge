def maxIncreasingDumbbellsSum(rack, n):
    def tabulation():
        dp = [ [0]*(n+1) for _ in range(n+1) ]

        for idx in range(n-1,-1,-1):
            for prev_idx in range(idx-1,-2,-1):

                not_take = 0 + dp[idx+1][prev_idx+1] # Dont take current index
                
                take = 0
                if prev_idx == -1 or rack[idx] > rack[prev_idx]:
                    take = rack[idx] + dp[idx+1][idx+1] # Take current index
                
                dp[idx][prev_idx+1] = max(take, not_take)
        
        return dp[0][-1+1]
    return tabulation()