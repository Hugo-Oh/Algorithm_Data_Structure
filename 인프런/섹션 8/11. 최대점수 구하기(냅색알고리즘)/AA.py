import sys
#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

arr = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(M+1)] #dp[i] = i초일때 얻을 수 있는 최대 스코어
for s, t in arr:
    for tot_s in range(M, t-1, -1):
        dp[tot_s] = max(dp[tot_s], dp[tot_s - t] + s)

print(dp[M])



