import sys
from _collections import deque
import heapq as hq
sys.stdin = open("input.txt", "rt")
#input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
heap = []
for _ in range(M):
    pre, post = map(int, input().split())
    graph[pre].append(post)
    degree[post] += 1

for i in range(1, N+1):
    if degree[i] == 0:
        hq.heappush(heap, i)

while heap:
    now = hq.heappop(heap)
    print(now, end = " ")
    for next in graph[now]:
        degree[next] -= 1
        if degree[next] == 0:
            hq.heappush(heap, next)

#우선순위 큐?


