def subsets(arr, i, n, k, sum_, subset, res):
    # if index "i" is same as length "n" of array and
    # "sum_" is same as "k", "subset" is appended to "res"
    if i == n:
        if sum_ == k:
            res.append(subset)
        return
    
    # current value is considered by adding it to "sum_" and
    # appending it to "subset"
    subsets(arr, i + 1, n, k, sum_ + arr[i], subset + [arr[i]], res)
    
    # current value is not considered
    subsets(arr, i + 1, n, k, sum_, subset, res)

def findSubsetsThatSumToK(arr, n, k) :
    # initializing variables
    res = []
    
    # calling helper function
    subsets(arr, 0, n, k, 0, [], res)
    
    # finally returning "res"
    return res