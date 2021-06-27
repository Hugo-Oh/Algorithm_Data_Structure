import sys
from _collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def bfs():
    global max
    queue = deque()
    queue.extend(start)

    while queue:
        now_y, now_x = queue.popleft()
        if (now_y, now_x) not in visited:
            visited.append((now_y, now_x))
            for dy, dx in zip(ny, nx):
                next_y, next_x = now_y + dy, now_x + dx

                if 0 <= next_y < Y and 0 <= next_x < X and graph[next_y][next_x] == 0:
                    graph[next_y][next_x] = graph[now_y][now_x] + 1
                    queue.append((next_y, next_x))
                    if max < graph[next_y][next_x]:
                        max = graph[next_y][next_x]
    return

X, Y = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(Y)]
visited = []
start = []
for y in range(Y):
    for x in range(X):
        if graph[y][x] == 1:
            start.append((y, x))
nx = [1, -1, 0, 0]
ny = [0, 0, -1, 1]
max = 0

bfs()
for y in range(Y):
    for x in range(X):
        if graph[y][x] == 0:
            print(-1)
            sys.exit(0)
else:
    print(max - 1 if max > 1 else 0)


