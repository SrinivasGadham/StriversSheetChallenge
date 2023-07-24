def longestCommonPrefix(arr, n):
    # Write your code here
    # Return a string
    s=arr[0]
    if n==1:
        return s
    for i in range(1, n):
        j=0
        temp=''
        while j<len(s) and j<len(arr[i]):
            if arr[i][j]==s[j]:
                temp+=s[j]
            else:
                break
            j+=1
        s=temp
    return s