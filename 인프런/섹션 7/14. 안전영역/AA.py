import sys
sys.stdin=open("input.txt", "r")
#sys.setrecursionlimit(10**6)

N =int(input())
board = [list(map(int, input().split())) for _ in range(N)]


ny = [-1, 1, 0, 0]
nx = [0, 0, -1, 1]

def DFS(now_y, now_x, height):
    #board[now_y][now_x] = 0
    visit[now_y][now_x] = 1
    for dy, dx in zip(ny, nx):
        next_y = now_y + dy
        next_x = now_x + dx
        if 0 <= next_x < N and 0 <= next_y < N and visit[next_x][next_y] == 0:
            if board[next_y][next_x] > height:
                DFS(next_y, next_x, height)

res = 0
for height in range(1, 101):
    visit = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if board[y][x] > height and visit[y][x] == 0 :
                DFS(y, x, height)
                cnt += 1

    if cnt > res:
        print(height)
        res = cnt

print(res)