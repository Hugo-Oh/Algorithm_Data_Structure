import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

degree = [0 for _ in range(N+1)]
que = deque()
for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1
    degree[e] += 1

for i in range(N, 0, -1): # start 조건
    if degree[i] == 0:
        que.append(i)

while que:
    node = que.popleft()
    print(node, end = " ")
    for i in range(1, N+1):
        if graph[node][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                que.append(i)
                