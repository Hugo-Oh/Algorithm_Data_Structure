import sys
from _collections import deque
sys.stdin = open("input.txt", "rt")

Y, X = map(int, input().split())

graph = [list(map(int, input())) for _ in range(Y)]
graph = [[[x, 0, 0, 0] if x == 0 else [0, 0, 1, 0] for x in c] for c in graph] # 거리,방문, 벽, 벽방문
graph[0][0] = [1, 1]

start = (0, 0)
xs = [-1, 1, 0, 0]
ys = [0, 0, 1, -1]

def BFS():
    queue = deque()
    queue.append(start) #한개일때는 append, 그 이상일땐 extend
    while queue:
        now_y, now_x = queue.popleft()

        if now_y == Y-1 and now_x == X-1:
            print(graph[Y-1][X-1])
            return

        for dy, dx in zip(ys, xs):
            next_y = now_y + dy
            next_x = now_x + dx
            if 0 <= next_y < Y and 0 <= next_x < X: #조건 1
                if graph[next_y][next_x] == 1 and
                if graph[next_y][next_x][1:] == [0, 0]: #길인데 만난적 없으면
                    graph[next_y][next_x] = [graph[now_y][now_x][0] + 1, 1, 0]  # 걍 방문처리
                    queue.append((next_y, next_x))

                if graph[next_y][next_x][1:] == [1, 0]: #벽인데 만난적 없으면
                    graph[next_y][next_x] = [graph[now_y][now_x][0] + 1, 1, 1] # 만난적 있음
                    queue.append((next_y, next_x))




BFS()
for i in graph:
    print(i)




