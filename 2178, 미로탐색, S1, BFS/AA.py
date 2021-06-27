import sys
from _collections import deque
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
nx = [1, -1, 0, 0]
ny = [0, 0, -1, 1]
graph = [list(map(int, input())) for _ in range(N)]

def bfs(graph, y, x):
    queue = deque()
    queue.append((y, x))
    visited = []
    while queue:
        now_y, now_x = queue.popleft()
        if (now_y, now_x) not in visited:
            visited.append((now_y, now_x))

            for dx, dy in zip(nx, ny):
                next_x = now_x + dx
                next_y = now_y + dy

                if not (0 <= next_x < M and 0 <= next_y < N) or graph[next_y][next_x] == 0:
                    continue

                if 0 <= next_x < M and 0 <= next_y < N and graph[next_y][next_x] == 1 and (next_y, next_x) not in visited:
                        graph[next_y][next_x] = graph[now_y][now_x] + 1
                        queue.append((next_y, next_x))

    return

bfs(graph, 0, 0)
print(graph[N-1][M-1])




#distance = [[-1 for _ in range(M)] for _ in range(N)]

#for i in graph:
#    print(i)

#queue = deque([0, 0])
#distance[0][0] = 1

"""def bfs(y, x):
    global distance
    if y < 0 or x < 0 or x >= M or y >= N:
        return

    if graph[y][x] == 0 or visited[y][x] == 1:
        return

    else:
        visited[y][x] = 1
        graph[y][x] = distance + 1
        distance += 1

        """


"""bfs(0, 0)

for i in graph:
    print(i)





"""

"""
def BFS(y, x):
    distance = []
    visited = [[0 for _ in range(M)] for _ in range(N)]

    if y < 0 or x < 0 or x >= N or y >= N:
        return

    if graph[y][x] == 0:
        return

    while queue:
        queue.popleft()


    while queue:

"""


