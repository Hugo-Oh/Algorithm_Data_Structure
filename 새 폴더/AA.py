import sys

#sys.stdin = open("input.txt", "rt")

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * i for i in range(1,N + 1)]

dp[0][0] = graph[0][0]
for i in range(N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][0] + graph[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][-1] + graph[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + graph[i][j], dp[i-1][j] + graph[i][j])

print(max(dp[N-1]))

