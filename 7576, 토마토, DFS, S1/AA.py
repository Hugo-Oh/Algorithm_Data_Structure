import sys
sys.stdin = open('input.txt',"rt")

N,M = map(int,input().split())
graph = []
for i in range(M):
    graph.append(list(map(int,input().split())))

print(graph)
result=0
def dfs(r,c):
    global result
    if r < 0 or r >= M or c < 0 or c >= N:
        return False

    if graph[r][c] == 0:
        return False

    result += 1
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for _ in range(4):
        if 0 <= r+dr[_] < M and 0 <= c + dc[_] < N:
            graph[r+dr[_]][c+dc[_]] = 1
            dfs(r+dr[_],c+dc[_])
        else:
            return False
    return True


for r in range(M):
    for c in range(N):
        if graph[r][c] == 1:
            print(dfs(r, c))

print(result)
for i in graph:
    print(i)