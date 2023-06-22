def findIslands(mat, n, m):
	def dfs(row,column):
		if visited[row][column]==True:
			return
		visited[row][column]=True
		for dir in range(8):
			new_x,new_y=row+id_x[dir],column+id_y[dir]
			if isValid(new_x,new_y,visited):
				dfs(new_x,new_y)

	id_x=[0,0,-1,1,-1,-1,1,1]
	id_y=[1,-1,0,0,1,-1,-1,1]
	def isValid(x,y,visited):
		if x>=0 and x<n and y>=0 and y<m and visited[x][y]==False and mat[x][y] == 1:
			return True
		return False
	visited=[[False for i in range(m)] for i in range(n)]
	count=0
	for i in range(n):
		for j in range(m):
			if mat[i][j]==1 and visited[i][j]==False:
				count+=1
				dfs(i,j)
	return count



	