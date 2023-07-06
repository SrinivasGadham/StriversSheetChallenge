def check(s, left, right):
    
    n = len(s)
    while left >= 0 and right < n:
        if s[left] != s[right]:
            break
        left -= 1
        right += 1
    return s[left+1:right]

def longestPalinSubstring(string):
    
    longest = ""
    n = len(string)
    for i in range(n):
        odd = check(string, i, i)
        if len(odd) > len(longest):
            longest = odd
    for i in range(n):
        even = check(string, i, i+1)
        if len(even) > len(longest):
            longest = even
    return longest