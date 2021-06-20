import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)


T = int(input())
res = []
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]


    for _ in range(K):
        r, c = map(int, input().split())
        arr[c][r] = 1

    def DFS(r, c):
        if r < 0 or r >= N or c < 0 or c >= M:
            return

        if arr[r][c] in (0, "visited"):
            return

        arr[r][c] = "visited"
        DFS(r-1, c)
        DFS(r+1, c)
        DFS(r, c-1)
        DFS(r, c+1)

    cnt = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                DFS(r, c)
                cnt += 1

    res.append(cnt)

for i in res:
    print(i)