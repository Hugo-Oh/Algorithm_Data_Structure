import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
ch = [[0 for _ in range(N)] for _ in range(N)]

ny = [1, 0 ,-1, 0]
nx = [0, 1, 0, -1]
minn = 21470000
maxx = -21470000
s_x = 0
s_y = 0
e_x = 0
e_y = 0

for y in range(N):
    for x in range(N):
        if board[y][x] < minn:
            minn = board[y][x]
            s_x = x
            s_y = y
        elif board[y][x] > maxx:
            maxx = board[y][x]
            e_x = x
            e_y = y

answer = 0

def DFS(now_y, now_x):
    global answer
    if now_y == e_y and now_x == e_x:
        answer += 1
        return
    else:
        for dy, dx in zip(ny, nx):
            next_y = now_y + dy
            next_x = now_x + dx
            if 0 <= next_y < N and 0 <= next_x < N:
                if board[next_y][next_x] > board[now_y][now_x] and ch[next_y][next_x] == 0:
                    ch[next_y][next_x] = 1
                    DFS(next_y, next_x)
                    ch[next_y][next_x] = 0

DFS(s_y, s_x)
print(answer)
