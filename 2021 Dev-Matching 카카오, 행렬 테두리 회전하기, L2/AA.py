from _collections import deque
columns = 4
rows = 5
board = [list(range((i-1) * columns + 1, (i-1) * columns + columns + 1)) for i in range(1, rows+1)]

que = deque()

def clockwise(x1, y1, x2, y2):
    x_ran = abs(x2 - x1)
    y_ran = abs(y2 - y1)
    cnt = 0



            # if y == y1 and x == x1:
            #     board[y-1][x-1] = board[y][x-1]
            #
            # elif y == y1 and x == x2:
            #     board[y-1][x-1] = board[y-1][x-2]
            # elif y == y2 and x == x1:
            #     board[y-1][x-1] = board[y-1][x]
            # elif y == y2 and x == x2:
            #     board[y-1][x-1] = board[y-2][x-1]
            # #elif y in (y1, y2) or x in (x1, x2):
            # #    board[y-1][x-1] = board[y-1][x-1] + 1
            # else:
            #     pass


    return board

clockwise(1,1,3,3)
print(que)
for i in board:
    print(i)