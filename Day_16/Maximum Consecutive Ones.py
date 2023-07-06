
def longestSubSeg(arr, n, k):
    zero_count=0
    ans=0
    i=0
    for j in range(n):
        if arr[j]==0:
            zero_count+=1
        while (zero_count>k):
            if arr[i]==0:
                zero_count-=1
            i+=1
        ans=max(ans,j-i+1)
    return ans
            