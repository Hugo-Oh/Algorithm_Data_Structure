import sys
<<<<<<< HEAD
#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

graph = [[214700000 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    s, e, cost = map(int, input().split())
    graph[s][e] = cost
    
for s in range(1, N+1):
    for e in range(1, N+1):
        if s == e:
            graph[s][e] = 0
            
for k in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])

for s in range(1, N+1):
    for e in range(1, N+1):
        if graph[s][e] == 214700000:
            print("M", end = " ")
        else:
            print(graph[s][e], end = " ")
    print()
=======
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
>>>>>>> 12f586e6b02d24679e5a3438eed3e6f0e609487b
