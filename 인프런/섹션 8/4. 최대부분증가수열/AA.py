import sys
sys.stdin = open("in1.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]


def DFS(L):
    if L == 0:
        return 1
    else:
        for before in range(L-1, -1, -1):
            if arr[before] < arr[L]:
                dp[L] = max(DFS(before) + 1, dp[L])
        return dp[L]
DFS(N-1)

