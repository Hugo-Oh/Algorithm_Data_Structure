from collections import deque
import sys
from itertools import combinations

sys.stdin = open("input.txt", "rt")

subtot = 0
N, M = map(int, input().split())
dis = [[0 for _ in range(N)] for _ in range(N)]
nx = [1, 0, -1, 0]
ny = [0, 1, 0, -1]
visit = [[0 for _ in range(N)] for _ in range(N)]
graph = [list(map(int, input().split())) for _ in range(N)]
def BFS(): #graph[now_y][now_x] == 2로 시작
    global subtot
    que = deque()
    que.extend([(0, 2), (1, 2)])
    
    while que:
        now_y, now_x = que.popleft() #하나하나 할 것임
        visit[now_y][now_x] = 1
        if graph[now_y][now_x] == 1:
            subtot += dis[now_y][now_x]
        
        for dy, dx in zip(ny, nx):
            next_y, next_x = now_y + dy, now_x + dx
            if 0 <= next_y < N and 0 <= next_x < N and visit[next_y][next_x] == 0 and graph[next_y][next_x] != 2:
                dis[next_y][next_x] = dis[now_y][now_x] + 1
                que.append((next_y, next_x))

BFS()
for c in dis:
    print(c)
print(subtot)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

start = []
for y in range(N):
    for x in range(N):
        if graph[y][x] == 2:
            start.append((y,x))
print(start)

"""for s in :combinations(start, 3)
    if len(s) == 1:
        que.append(s)
    else:
        que.extend(s)
"""
nx = [1, 0, -1, 0]
ny = [0, 1, 0, -1]
tot = 0

res = []
while start:
    y, x = start.pop()
    dis = [[0 for _ in range(N)] for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    subtot = 0
    BFS(y, x)
    res.append(subtot)

               






"""for y in range(N):
    for x in range(N):
        if graph[y][x] == 2:
            start.append((y, x))
que = deque()
ny = [1, 0, -1, 0]
nx = [0, 1, 0, -1]
if len(start) == 1:
    que.append(start)
else:
    que.extend(start)

DFS()

for r in graph:
    print(r)"""