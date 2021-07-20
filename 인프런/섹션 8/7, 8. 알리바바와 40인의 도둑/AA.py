import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]

for y in range(N):
    for x in range(N):
        if y == 0 and x == 0:
            dp[y][x] = graph[y][x]

        elif y == 0: # x >= 1
            dp[y][x] = dp[y][x-1] + graph[y][x]

        elif x == 0: # y >= 1
            dp[y][x] = dp[y-1][x] + graph[y][x]

        else:
            dp[y][x] = graph[y][x] + min(dp[y-1][x], dp[y][x-1])

print(dp[N-1][N-1])
