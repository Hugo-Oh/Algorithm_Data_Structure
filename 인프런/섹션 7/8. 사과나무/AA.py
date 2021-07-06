import sys
from _collections import deque
sys.stdin = open("input.txt", "rt")

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visit=[[0]*N for _ in range(N)]


s = N // 2
que = deque()
res = graph[s][s]
visit[s][s] = 1
ny = [-1, 1, 0, 0]
nx = [0, 0, -1, 1]
def BFS():
    global res
    que.append((s, s))
    while que:
        now_y, now_x = que.popleft()
        for dy, dx in zip(ny, nx):
            next_y = now_y + dy
            next_x = now_x + dx
            if 0 <= next_x < N and 0 <= next_y < N:
                if visit[next_y][next_x] == 0 and visit[now_y][now_x] <= s:
                    visit[next_y][next_x] = visit[now_y][now_x] + 1
                    res += graph[next_y][next_x]
                    que.append((next_y, next_x))
                    #print(next_y, next_x)
    return
BFS()
print(res)
