import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
arr = list(map(int, input().split()))

print(arr)

dp[n] = dp[n-1]

