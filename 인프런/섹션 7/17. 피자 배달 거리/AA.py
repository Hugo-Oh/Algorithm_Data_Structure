from collections import deque
import sys
from itertools import combinations

#sys.stdin = open("in1.txt", "rt")

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
answer = 21470000

ny = [0, 1, 0, -1]
nx = [1, 0, -1, 0]
starts = []
for y in range(N):
    for x in range(N):
        if graph[y][x] == 2:
            starts.append((y, x))

for start in combinations(starts, M):
    visit = [[0 for _ in range(N)] for _ in range(N)]
    dis = [[0 for _ in range(N)] for _ in range(N)]
    que = deque()
    tot = 0
    
    if len(start) == 1:
        que.append(start)
    else:
        que.extend(start)

    for y, x in que:
        visit[y][x] = 1

    while que:
        now_y, now_x = que.popleft()
        if graph[now_y][now_x] == 1:
            tot += dis[now_y][now_x]
            
        for dy, dx in zip(ny, nx):
            next_y, next_x = now_y + dy, now_x + dx
            if 0 <= next_y < N and 0 <= next_x < N and visit[next_y][next_x] == 0:
                dis[next_y][next_x] = dis[now_y][now_x] + 1
                visit[next_y][next_x] = 1
                que.append((next_y, next_x))
    
    if tot < answer:
        answer = tot

print(answer)




