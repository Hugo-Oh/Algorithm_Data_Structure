import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
coin = list(map(int, input().split()))
change = int(input())

dp = [1000 for _ in range(change + 1)]
dp[0] = 0
for c in coin:
    for tot_c in range(c, change + 1):
        dp[tot_c] = min(dp[tot_c], dp[tot_c - c] + 1)
        
print(dp[change])