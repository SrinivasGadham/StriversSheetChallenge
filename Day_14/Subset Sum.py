from typing import List
def cal(ind,res,num,N,ans):
    if ind==N:
        ans.append(res)
        return
    cal(ind+1,res+num[ind],num,N,ans)
    cal(ind+1, res, num,N, ans)

def subsetSum(num):
    N=len(num)
    ans=[]
    cal(0,0,num,N,ans)
    ans.sort()
    return ans