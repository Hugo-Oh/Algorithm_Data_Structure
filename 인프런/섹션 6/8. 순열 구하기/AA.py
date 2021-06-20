import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split()) # 3 2
arr = list(range(1, N+1))

check = [0] * N
res = [0] * M

def DFS(L):
    if L == M:
        for i in res:
            print(i, end = " ")
        print()
        return

    else:
        for i in range(N):
            if check[i] == 0:
                check[i] = 1
                res[L] = arr[i]
                DFS(L+1)
                check[i] = 0

DFS(0)


