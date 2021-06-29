import sys
from _collections import deque
sys.stdin = open("input.txt", "rt")

Y, X = map(int, input().split())

graph = [list(map(int, input())) for _ in range(Y)]
graph = [[[x, "nvisit"] if x == 0 else [0, "wall"] for x in c] for c in graph]
graph[0][0] = [0, 'visit']
ny = [0, 0, 1, -1]
nx = [1, -1, 0, 0]
# 단순히 순회하는 것

def BFS():
    start = (0, 0)
    queue = deque()
    queue.append(start)

    while queue:
        now_y, now_x = queue.popleft()
        if now_x == X-1 and now_y == Y-1:
            print(graph[now_y][now_x])

        else:
            for dy, dx in zip(ny, nx):
                next_y = now_y + dy
                next_x = now_x + dx
                if 0 <= next_y < Y and 0 <= next_x < X:
                    if graph[next_y][next_x][1] == 'nvisit':
                        graph[next_y][next_x] = [graph[now_y][now_x][0] + 1, 'visit']
                        queue.append((next_y, next_x))



BFS()
for i in graph:
    print(i)
