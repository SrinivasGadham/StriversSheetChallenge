from typing import List

def combinationSum2(arr: List[int], n: int, target: int) -> List[List[int]]:
    candidates=arr
    n=len(candidates)
    l=candidates
    l.sort()
    res=[]
    def f(ind,tar,arr):
        if tar==0:
            res.append(arr.copy())
            return
        for i in range(ind,n):
            if i>ind and l[i]==l[i-1]:
                continue
            if l[i]>tar:
                break
            arr.append(l[i])
            f(i+1,tar-l[i],arr)
            arr.pop()
    f(0,target,[])

    return res