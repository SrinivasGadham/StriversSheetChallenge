def kthSmallLarge(arr, n, k):
    l=[]
    arr.sort()
    a=arr[::-1]
    #kth smallest number in ascending sorted array
    l.append(arr[k-1])
    #kth largest number in descending sorted array
    l.append(a[k-1])
    
    return l
    