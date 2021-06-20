import sys
#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
arr = [0] * M

cnt = 0
def DFS(n):
    global cnt
    if n == M:
        for i in arr:
            print(i, end = " ")
        print()
        cnt += 1
        return

    else:
        for i in range(1, N + 1):
            arr[n] = i
            DFS(n+1)


DFS(0)
print(cnt)
