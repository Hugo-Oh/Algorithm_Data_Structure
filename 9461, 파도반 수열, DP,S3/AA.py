import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
for _ in range(N):
    n = int(input())
    dp = [1 for _ in range(100)]

    def padoban(n):
        if n < 3:
            res = dp[n]
            return res

        else:
            for i in range(3, n+1):
                dp[i] = dp[i-2] + dp[i-3]
            res = dp[n]
            return res

    print(padoban(n-1))