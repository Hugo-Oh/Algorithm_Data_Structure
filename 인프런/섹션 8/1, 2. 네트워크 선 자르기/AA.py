#N = int(input())
N = 7

"""dp = [0 for _ in range(N)]

dp[0] = 1
dp[1] = 2

for i in range(2, N):
    dp[i] = dp[i-2] + dp[i-1]
#print(dp)
print(dp[N-1])"""

dp = [0 for _ in range(N)]
def DFS(N):
    if dp[N] != 0:
        return dp[N]
    
    if N == 0:
        return 1
    
    if N == 1:
        return 2
    
    else:
        dp[N] = DFS(N-1) + DFS(N-2)
        return dp[N]

print(DFS(N-1))
