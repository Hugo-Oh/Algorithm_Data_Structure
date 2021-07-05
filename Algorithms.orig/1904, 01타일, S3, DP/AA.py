import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

dp = [1, 2]

def tiles(n):
    if n < 2:
        return dp[n]

    else:
        for i in range(2, n+1):
            dp.append((dp[i-2] + dp[i-1]) % 15746)
        return dp[n]

print(tiles(n-1))
