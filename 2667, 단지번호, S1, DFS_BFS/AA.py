import sys
"""sys.stdin = open("input.txt", "rt")

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

def dfs(y, x):
    if y < 0 or y >= N or x < 0 or x >= N:
        return
    
    if 


"""
sys.stdin = open("input.txt", "rt")

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
address = 0

nx = [1, -1, 0, 0]
ny = [0, 0, -1, 1]
cnt = 0
def dfs(y, x):
    global address, cnt
    if y < 0 or y >= N or x < 0 or x >= N:
        return

    if graph[y][x] == 0 or visited[y][x] == 1:
        return

    visited[y][x] = 1
    graph[y][x]   = address + 1
    cnt += 1
    for dx, dy in zip(nx, ny):
        dfs(y + dy, x + dx)

res = []
for y in range(N):
    for x in range(N):
        if graph[y][x] == 1 and not visited[y][x]:
            dfs(y, x)
            address += 1
            res.append(cnt)
            cnt = 0


print(address)
for i in sorted(res):
    print(i)