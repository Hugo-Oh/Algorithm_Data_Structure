from collections import deque
import sys
sys.stdin = open("input.txt", "rt")
N,M=map(int,sys.stdin.readline().split())
temp=[[0]*M for i in range(N)]
data=[]
for i in range(N):
  data.append(list(map(int,sys.stdin.readline().rstrip())))

def bfs(x,y):
  dx=[0,0,-1,1]
  dy=[1,-1,0,0]
  q=deque()
  q.append((x,y))
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx>=0 and ny>=0 and nx<N and ny<M:
        if temp[nx][ny]==0:
          temp[nx][ny]=temp[x][y]+1
          if nx==N-1 and ny==M-1:break
          q.append((nx,ny))
  return temp[N-1][M-1]+1
result=0

def break_wall(count):
  global result
  if count==1:
    for i in range(N):
      for j in range(M):
        temp[i][j]=datad[i][j]
    result=max(result,bfㅣs(0,0))
    return
  for i in range(N):
    for j in range(M):
      if data[i][j]==1:
        data[i][j]=0
        count+=1
        break_wall(count)
        count-=1
        data[i][j]=1
break_wall(0)
if result==1:print(-1)
else:print(result)