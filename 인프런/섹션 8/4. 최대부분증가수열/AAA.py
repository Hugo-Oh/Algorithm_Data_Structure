import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

print(arr)
#dp[i] = i번쨰 인덱스일때의 증가수열의 최대길이
#dp[0] = 1
dp = [1 for _ in range(n)]
for now in range(n):
    for before in range(now):
        if arr[now] > arr[before]:
            dp[now] = max(dp[before] + 1, dp[now])

print(max(dp))



