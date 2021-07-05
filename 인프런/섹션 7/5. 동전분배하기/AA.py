import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
coin = [int(input()) for _ in range(N)]

arr = [0, 0, 0]
res = 21470000
def DFS(L):
    global res
    if L == N:
        cha = max(arr) - min(arr)
        if cha < res and len(set(arr)) == 3:
            res = cha
        return
    else:
        for i in range(len(arr)):
            arr[i] += coin[L]
            DFS(L+1)
            arr[i] -= coin[L]
DFS(0)
print(res)

