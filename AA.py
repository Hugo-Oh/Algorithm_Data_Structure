import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [1, 0]
dp[2] = [1, 1]
dp[1] = [1, 0]
dp[3] = [2, 1]

for i in range(4, 41):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    dp[i][1] = dp[i - 1][0]

N = int(input())
M = int(input())
arr = [int(input()) for _ in range(M)]
s = 1


if N+1 not in arr:
    arr.append(N+1)
res = 1
for vip in arr:
    gap = vip - s
    s = vip + 1
    res *= sum(dp[gap])

print(res)








