import sys
#sys.stdin = open("input.txt", "rt")


N =int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ch = [[0 for _ in range(N)] for _ in range(N)]
nx = [-1, -1, -1, 0, 0, 1, 1, 1]
ny = [0, -1,  1, 1, -1, 1, -1, 0]
cnt = 0
def DFS(now_y, now_x):
    global cnt
    for dy, dx in zip(ny, nx):
        board[now_y][now_x] = 0
        next_y = now_y + dy
        next_x = now_x + dx
        if 0 <= next_y < N and 0 <= next_x < N:
            if board[next_y][next_x] == 1 and ch[next_y][next_x] == 0:
                ch[next_y][next_x] = 1
                DFS(next_y, next_x)

for y in range(N):
    for x in range(N):
        if board[y][x] == 1 and ch[y][x] == 0:
            DFS(y, x)
            cnt += 1

print(cnt)




