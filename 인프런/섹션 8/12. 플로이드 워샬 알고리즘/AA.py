import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
#1번 플로이드 워셜!
inf = 21470000
graph = [[inf for _ in range(N+1)] for _ in range(N+1)]
#dp = [[inf for _ in range(N+1)] for _ in range(N+1)] #

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s][e] = c

dp = [inf for _ in range(N+1)]
for i in range(1, N+1):
    dp[i] = graph[1][i]
dp[1] = 0
for i in graph:
    print(i)
print()
for now in range(1, N+1):
    for k in range(1, N+1):
        graph[now] = min(graph[1][now], graph[now][1])
print(dp)