import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())

data = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * 16
#dp[n] = dp[n]일에 얻을 수 있는 최대 점수의 합
#LIS문제긴 해
#n번째, m은 뭐지, income, 상담이 가능한지도 생각해봐야지.
#메모이제이션은 나중에 하자.

res = 0

def DFS(L, tot):
    global res
    if L == N+1:
        if tot > res:
            res = tot

    else:
        if L + data[L][0] <= N+1:
            DFS(L+data[L][0], tot + data[L][1])
        DFS(L+1, tot)

data.insert(0, (0, 0))

DFS(1, 0)

print(res)


