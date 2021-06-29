import sys
from _collections import deque
sys.stdin = open("input.txt", "rt")

X, Y = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(Y)]
ny = [-1, +1, 0, 0]
nx = [0, 0, -1, +1]
start = []

for y in range(Y):
    for x in range(X):
        if graph[y][x] == 1:
            start.append((y, x))

queue = deque()
queue.append(start)

maxx = -1

def BFS():
    global maxx
    queue = deque()
    queue.extend(start)
    while queue:
        now_y, now_x = queue.popleft()

        for dy, dx in zip(ny, nx) :
            next_y = now_y + dy
            next_x = now_x + dx
            if 0 <= next_y < Y and 0 <= next_x < X and graph[next_y][next_x] == 0 :
                graph[next_y][next_x] = graph[now_y][now_x] + 1
                if graph[next_y][next_x] > maxx:
                    maxx = graph[next_y][next_x]
                queue.append((next_y, next_x))
BFS()
for row in graph:
    if 0 in row:
        print(-1)
        break
else:
    print(maxx - 1 if maxx > 1 else 0)
