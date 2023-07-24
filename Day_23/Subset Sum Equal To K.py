

def tabulation(n,target,arr):
    dp=[[False]*(target+1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = True
    
    for idx in range(0,n,1):
        for target in range(0,target+1,1):
            not_take=dp[idx-1][target]

            take=False
            if arr[idx]<=target:
                take=dp[idx-1][target-arr[idx]]
            
            dp[idx][target]=not_take or take

    return dp[idx][target]


def subsetSumToK(n, target, arr):
    
    
    

    
    return tabulation(n,target,arr)