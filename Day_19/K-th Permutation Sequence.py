def kthPermutation(n, k):
    ans=[]
    s=""
    res=""
    for i in range(1,n+1):
        s+=str(i)
    
    visited=[False]*(n)
    cnt=0
    def f(s,res,visited,ans,k):
        if len(res)==len(s):
            ans.append(res)
            nonlocal cnt
            cnt+=1
            if cnt==k:
                return
    
    
    
        for i in range(0,len(s)):
            if visited[i]==False:
                visited[i]=True
                res+=s[i]
                f(s,res,visited,ans,k)
                res=res[:len(res)-1]
                visited[i]=False
    
                if cnt==k:return
        
    f(s,res,visited,ans,k)
    return ans[-1]