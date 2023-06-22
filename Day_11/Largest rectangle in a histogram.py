def largestRectangle(arr):
    n=len(arr)
    ngri=[n for i in range(n)]
    stack=[]
    for i in range(n):
        while stack and arr[stack[-1]]>arr[i]:
            ngri[stack.pop()]=i
        stack.append(i)
    ngli=[-1 for i in range(n)]
    stack=[]
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]]>arr[i]:
            ngli[stack.pop()]=i
        stack.append(i)
    width=[]
    for i in range(n):
        width.append(ngri[i]-ngli[i]-1)
    max_ans=float('-inf')
    for i in range(n):
        max_ans=max(max_ans,width[i]*arr[i])
    return max_ans
    
    
    
    