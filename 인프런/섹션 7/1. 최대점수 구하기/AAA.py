import sys
#sys.stdin=open("input.txt", "rt")
N, M = map(int,input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]

res = -2149000
def DFS(L, Tot, Time):
    if L == N:
        global res
        return
    if Time > M:
        return
    else:
        if Tot > res:
            res = Tot
        DFS(L+1, Tot + arr[L][0], Time + Tot + arr[L][1])
        DFS(L + 1, Tot, Time)

DFS(0, 0, 0)
print(res)