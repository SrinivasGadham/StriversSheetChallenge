from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
def countWaysToMakeChange(arr, amount) :
    
    
    def tabulation(n,arr):
        dp = [ [0]*(amount+1) for _ in range(n)]

        for target in range(amount):
            dp[0][target] = target%arr[0]==0
        
        for i in range(1,n):
            for target in range(0,amount+1):
                not_take = memoization(i-1,target,arr,dp)
                take=0
                if arr[i]<=target:
                    take = memoization(i,target-arr[i],arr,dp)

                dp[i][target] = not_take + take

        return dp[i][target]
    
    n = len(arr)
    arr = sorted(arr)

    
    
    

    
    return tabulation(n,arr) 
































def takeInput() :
    numDenominations = int(input())

    denominations = list(map(int, stdin.readline().strip().split(" ")))

    value = int(input())
    return denominations, numDenominations, value



denominations, numDenomination, value = takeInput()
print((countWaysToMakeChange(denominations, value)))