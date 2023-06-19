m,n=3,3
mat=[[1,2,3],[4,5,6],[7,8,9]]
visited=[[False for i in range(m)] for i in range(n)]
id_x=[0,1,0,-1]
id_y=[1,0,-1,0]

start_i,start_j=0,0
dir=0
x,y=0,0
new=[[0 for i in range(m)] for i in range(n)]

while visited[start_i][start_j]==False:
    new_x,new_y=x+id_x[dir],y+id_y[dir]
    count=0
    for p in range(4):
        if new_x<0 or new_x>=n or new_y<0 or new_y>=m or visited[new_x][new_y]==True:
            dir=(dir+1)%4
            new_x,new_y=x+id_x[dir],y+id_y[dir]
            count+=1
        else:
            break
    if count==4:
        new[start_i][start_j]=mat[start_i][start_j]
        break
    
    new[new_x][new_y]=mat[x][y]
    visited[new_x][new_y]=True
    x,y=new_x,new_y
    if x==start_i and y==start_j:
        visited[start_i][start_j]=True
        x,y=start_i+1,start_j+1
        start_i,start_j=x,y
        dir=0
print(new)