import sys
from _collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def bfs():
    global max
    queue = deque()
    queue.extend(start) #초기 start 넣어주기

    while queue: #queue가 빌때까지
        now_y, now_x = queue.popleft() #queue
        if (now_y, now_x) not in visited: #방문하지 않았으면 방문처리하고
            visited.append((now_y, now_x))
            for dy, dx in zip(ny, nx): #그 다음노드 순회하기
                next_y, next_x = now_y + dy, now_x + dx #
                if 0 <= next_y < Y and 0 <= next_x < X and graph[next_y][next_x] == 0: #노드 정의가 되면(다음노드가 범위안에 있고, 방문하지 않앗고, 동시에 0이어야함)
                    graph[next_y][next_x] = graph[now_y][now_x] + 1 #지금노드보다 +1
                    queue.append((next_y, next_x)) #방문처리해서 다시 queue 순회
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
            start.append((y, x)) #start에 처음 1인곳 넣기

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


