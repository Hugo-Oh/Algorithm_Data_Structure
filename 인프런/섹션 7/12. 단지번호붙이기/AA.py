import sys
#sys.stdin = open("input.txt", "rt")


N =int(input())
board = [list(map(int, input())) for _ in range(N)]
ch = [[0 for _ in range(N)] for _ in range(N)]
address = 1
res = []
nx = [1, 0, -1, 0]
ny = [0, 1, 0, -1]
cnt = 0
def DFS(now_y, now_x):
    global cnt
    for dy, dx in zip(ny, nx):
        board[now_y][now_x] = address
        next_y = now_y + dy
        next_x = now_x + dx
        if 0 <= next_y < N and 0 <= next_x < N:
            if board[next_y][next_x] == 1 and ch[next_y][next_x] == 0:
                ch[next_y][next_x] = 1
                cnt += 1
                DFS(next_y, next_x)





for y in range(N):
    for x in range(N):
        if board[y][x] == 1 and ch[y][x] == 0:
            DFS(y, x)
            res.append(cnt)
            cnt = 1
            address += 1

print(address - 1)
for _ in sorted(res):
    print(_)

