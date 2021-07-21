import sys
from _collections import deque
#input = sys.stdin.readline
sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
que = deque()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1


for i in range(1, N+1):
    if degree[i] == 0:
        que.append(i)

while que:
    now = que.popleft()
    for search in graph[now]:
        degree[search] -= 1
        if degree[search] == 0:
            que.append(search)
    print(now, end=" ")



