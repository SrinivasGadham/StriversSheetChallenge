def palindromePartitioning(string):
    def memoization(i):
        if string[i:len(string)]==string[i:len(string)][::-1]:
            return 0

        if i == len(string):
            return 0
        
        if dp[i]!=-1:
            return dp[i]

        cost = float('inf')
        for j in range(i, len(string)):
            if string[i:j+1]==string[i:j+1][::-1]:
                cost = min(cost,1+memoization(j+1))
                dp[i] = cost
        
        return dp[i]

    dp = [-1]*len(string)
    return memoization(0) 