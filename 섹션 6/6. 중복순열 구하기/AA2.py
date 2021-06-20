"""import sys
sys.stdin = open("input.txt", "rt")
"""
N, M = map(int, input().split())

cnt = 0
def DFS(n):
    global cnt
    if n == M:
        for i in range(M):
            print(arr[i], end = " ")
        print()
        cnt += 1
        return

    else:
        for j in range(1, N+1):
            arr[n] = j
            DFS(n + 1)

arr = [0] * N
DFS(0)
print(cnt)

