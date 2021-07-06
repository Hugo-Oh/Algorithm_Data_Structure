import sys
sys.stdin = open("input.txt", "rt")

board = [list(map(int, input().split())) for _ in range(10)]

#좌 우 먼저 보고 # y는 그대로,
#그게 없으면 밑으로 간다
nx = [1, -1, 0]
ny = [0, 0, 1]
def DFS(now_y, now_x): #시작점은 각각.. 열번호는 now_x가 되겠져?
    if board[now_y][now_x] == 2:

        return True

    else:
        for dy, dx in zip(ny, nx):
            next_y = now_y + dy
            next_x = now_x + dx

            if 0 <= next_y < 10 and 0 <= next_x < 10:

                print(next_y, next_x)
                if board[next_y][next_x] == 1 and next_x == now_x + 1: #오른먼저
                    board[next_y][next_x] = 0
                    DFS(next_y, next_x)

                elif board[next_y][next_x] == 1 and next_x == now_x - 1: #왼쪽
                    board[next_y][next_x] = 0
                    DFS(next_y, next_x)

                else:
                    board[now_y][next_x] = 0
                    DFS(now_y + 1, now_x)

if DFS(0, 7):
    print("hi")
else:
    print("no")





