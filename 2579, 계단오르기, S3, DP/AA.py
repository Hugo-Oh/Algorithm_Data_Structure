import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

arr = [0]
dp = [0] * 1000

for _ in range(N):
    arr.append(int(input()))

for i in range(1, N+1):
    if i < 2:
        dp[i] = arr[i]
    elif i < 3:
        dp[i] = sum(arr[1:i+1])
    else:
        dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

res = dp[N]
print(res)