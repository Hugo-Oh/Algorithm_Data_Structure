import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]


    for _ in range(K):
        r, c = map(int, input().split())
        arr[c][r] = 1

    def DFS(r, c):
        dr = [1, -1, 0, 0]
        dc = [0, 0, -1, 1]

        if arr[r][c] == 1:
            arr[r][c] = "visited"
            for i in range(4):
                if 0 <= r + dr[i] < N and 0 <= c + dc[i] < M:
                    DFS(r + dr[i], c + dc[i])
            return True

        else:
            return False

    cnt = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                DFS(r, c)
                cnt += 1

    print(cnt)