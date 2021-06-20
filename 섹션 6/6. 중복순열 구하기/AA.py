import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split()) #3, 2

arr = list(range(1, N+1))
res = [0] * M
def DFS(L):
    if L == M:
        for i in res:
            print(i, end = " ")
        print()

    else:
        for i in range(N):
            res[L] = arr[i]
            DFS(L+1)

DFS(0)
print(arr)



