import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

arr = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]
#dp[i] = i번쨰 와인을 마실 떄 최대로 마시는 양
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
for i in range(2, n):
    dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i], dp[i-1])

print(max(dp))