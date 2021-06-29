from _collections import deque
import sys
sys.stdin = open("input.txt", "rt")

R = int(input())

for _ in range(R):
    N = int(input())
    cur_y, cur_x = map(int, input().split())
    tar_y, tar_x = map(int, input().split())

    #총 여덟군데 순회
    nx = [-2, -1, 1, 2, 2, 1, -1, -2]
    ny = [1, 2, 2, 1, -1, -2, -2, -1]
    graph = [[0 for _ in range(N)] for _ in range(N)]
    graph[cur_y][cur_x] = 1
    def bfs(y, x):
        queue = deque([])
        queue.append((y, x))
        while queue:
            y, x = queue.popleft()
            if x == tar_x and y == tar_y:
                return graph[y][x]

            for dy, dx in zip(ny, nx):  # 찾을때까지 다시 순환
                next_y = y + dy
                next_x = x + dx
                if 0 <= next_y < N and 0 <= next_x < N and not graph[next_y][next_x]:
                    graph[next_y][next_x] = graph[x][y] + 1
                    queue.append((next_y, next_x))

    x = bfs(cur_y, cur_x)
    print(x-1 if x > 0 else 0)
