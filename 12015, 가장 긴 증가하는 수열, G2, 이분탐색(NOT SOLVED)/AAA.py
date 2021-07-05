import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
arr = list(map(int, input().split()))

dp=[1 for _ in range(n)]
#dp[0] = 1 #기저조건
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])

#dp = [x if x > 0 else 1 for x in dp]

print(dp)

