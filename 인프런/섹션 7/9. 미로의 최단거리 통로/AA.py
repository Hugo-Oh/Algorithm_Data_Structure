import sys
from _collections import deque
#   sys.stdin = open("input.txt", "rt")
nx = [-1, 0, 1, 0]
ny = [0, 1, 0, -1]

graph = [list(map(int, input().split())) for _ in range(7)]
ch = [[0 for _ in range(7)] for _ in range(7)]

que = deque()
que.append((0, 0))
graph[0][0] = 1

while que:
    now_y, now_x = que.popleft()

    for dy, dx in zip(ny, nx):
        next_y = now_y + dy
        next_x = now_x + dx
        if 0 <= next_y < 7 and 0 <= next_x < 7 and graph[next_y][next_x] == 0:
            graph[next_y][next_x] = 1 #방문처리 하고
            ch[next_y][next_x] = ch[now_y][now_x] + 1 #거리 구하고
            que.append((next_y, next_x))


print(ch[6][6] if ch[6][6] else -1)

