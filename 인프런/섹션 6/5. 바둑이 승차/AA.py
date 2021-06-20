import sys
#sys.stdin = open("in1.txt", "rt")

CAP, M = map(int, input().split())
arr = []

for _ in range(M):
    arr.append(int(input()))

res = 0
tot = sum(arr)

def DFS(L, W, TOT):
    global res
    if W > CAP:
        return

    if W + (tot - TOT) < res:
        return

    if L == M:
        if W > res:
            res = W
        return


    else:
        DFS(L+1, W + arr[L], TOT + arr[L])
        DFS(L+1, W, TOT + arr[L])

DFS(0,0,0)

print(res)
