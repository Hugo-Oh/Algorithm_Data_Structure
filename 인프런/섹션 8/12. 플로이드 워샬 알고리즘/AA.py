import sys
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