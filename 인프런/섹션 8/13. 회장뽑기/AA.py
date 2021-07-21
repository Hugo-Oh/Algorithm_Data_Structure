import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())

graph = [[21470000 for _ in range(N+1)] for _ in range(N+1)]

while True:
    s, e = map(int, input().split())
    if (s, e) == (-1, -1):
        break
    else:
        graph[s][e] = 1
        graph[e][s] = 1

for s in range(1, N+1):
    for e in range(1, N+1):
        if s == e:
            graph[s][e] = 0

for k in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])
            
check = [max(x[1:]) for x in graph[1:]]
minn = min(check)

print(minn, check.count(minn))
for i in range(1, N+1):
    if check[i-1] == min(check):
        print(i, end = " ")


