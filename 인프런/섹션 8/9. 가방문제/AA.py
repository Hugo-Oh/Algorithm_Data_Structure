import sys

# sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

arr = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(M + 1)]
for w, v in arr:
    for tot_v in range(w, M + 1):
        dp[tot_v] = max(dp[tot_v], dp[tot_v - w] + v)

print(dp[M])



