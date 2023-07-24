def memoization(e, f, dp):
    
    if f <= 1 or e == 1:
        return f

    if dp[e][f] != -1:
        return dp[e][f]

    
    ans = float('inf')
    start, end = 1, f
    while start <= end:
        mid = (start + end) // 2

        BREAK = memoization(e - 1, mid - 1, dp)
        SURVIVE = memoization(e, f - mid, dp)

        
        ans = min(ans, 1 + max(BREAK, SURVIVE))

        if BREAK < SURVIVE:
            start = mid + 1
        else:
            end = mid - 1

    dp[e][f] = ans
    return ans

def cutLogs(k, n):
   
    dp = [[-1] * (n + 1) for _ in range(k + 1)]
    return memoization(k, n, dp)