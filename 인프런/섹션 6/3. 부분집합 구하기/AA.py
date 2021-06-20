import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))

check = [0] * N
def DFS(L):
    if L == N:
        for i in range(N):
            if check[i] == 1:
                print(arr[i], end = " ")
        print()

    else:
        check[L] = 1
        DFS(L+1)
        check[L] = 0
        DFS(L+1)

DFS(0)
