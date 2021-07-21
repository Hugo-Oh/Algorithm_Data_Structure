import sys
from collections import deque

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    cost = list(map(int, input().split()))
    cost.insert(0, 0)

    graph = [list() for _ in range(N+1)]
    degree = [0 for _ in range(N+1)]
    que =deque()
    dp = [0 for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        degree[b] += 1

    W = int(input())

    for i in range(1, N+1):
        if degree[i] == 0:
            que.append(i)
            dp[i] = cost[i]

    while que:
        now = que.popleft()
        if now == W:
            print(dp[now])

        for detect in graph[now]:
            degree[detect] -= 1
            dp[detect] = max(dp[detect], dp[now] + cost[detect])
            if degree[detect] == 0:
                que.append(detect)


