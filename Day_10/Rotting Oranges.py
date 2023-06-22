def minTimeToRot(grid, n, m):
    from queue import Queue

    minTime,numOrange=-1,0
    def isValid(r,c):
        if r<0 or r>=n: return False
        if c<0 or c>=m: return False
        if grid[r][c]!=1: return False
        return True
    queue=[]
    
    for r in range(n):
        for c in range(m):
            if grid[r][c]==2:
                queue.append((r,c))
            if grid[r][c]!=0:
                numOrange+=1
    
    if numOrange==0: return 0
    
    while queue:
        
        minTime+=1
        for _ in range(len(queue)):
            
            r,c=queue.pop(0)
            
            nei=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for r1,c1 in nei:
                if isValid(r1,c1):
                    grid[r1][c1]=2
                    queue.append((r1,c1))

    for r in range(n):
        for c in range(m): 
            if grid[r][c]==1: return -1
    return minTime     