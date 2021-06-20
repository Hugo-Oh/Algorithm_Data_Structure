import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
arr = sorted(list(map(int,input().split())), reverse = True)
C = int(input())

res = 21470000

def DFS(L, c):
    global res

    if L >= res:
        return

    if c < 0:
        return

    if c == 0:
        if L < res:
            res = L

    else:
        for i in range(N):
            DFS(L+1, c - arr[i])

DFS(0, C)
print(res)