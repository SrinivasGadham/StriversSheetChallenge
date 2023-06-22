def nextSmallerElement(arr,n):
    ngri=[-1 for i in range(n)]
    stack=[]
    for i in range(n):
        while stack and arr[stack[-1]]>arr[i]:
            ngri[stack.pop()]=i
        stack.append(i)
    ngr=[]
    for i in range(n):
        if ngri[i]!=-1:
            ngr.append(arr[ngri[i]])
        else:
            ngr.append(-1)
    return ngr