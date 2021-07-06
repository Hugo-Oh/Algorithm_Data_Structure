#미로탐색(DFS)
import sys
sys.stdin = open("input.txt", "rt")

board = [list(map(int, input().split())) for _ in range(7)]
board[0][0] = 1
answer = 0

ny = [1, 0, -1, 0]
nx = [0, 1, 0, -1]

def DFS(now_y, now_x):
    global answer
    if now_y == 6 and now_x == 6:
        answer += 1
        return

    else:
        for dy, dx in zip(ny, nx):
            next_y = now_y + dy
            next_x = now_x + dx
            if 0 <= next_y < 7 and 0 <= next_x < 7 and board[next_y][next_x] == 0:
                board[next_y][next_x] = 1
                DFS(next_y, next_x)
                board[next_y][next_x] = 0

DFS(0, 0)
print(answer)





