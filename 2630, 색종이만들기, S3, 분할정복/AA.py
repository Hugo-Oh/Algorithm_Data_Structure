import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

one = 0
zero = 0
def dom(board):
    global one, zero
    for i in board:
        print(i)

    if len(board) == 1:

        if board[0] == 1:
            one += 1

        return

    if all([all(x) for x in board]): #모두 1이거나
        one += 1
        print("one")
        print()

    elif all([not any(x) for x in board]): #모두 0
        zero += 1
        print("zero")
        print()

    else: #단 하나라도 0이 있다면

        N = len(board)
        # 4분할 운동..

        A = [x[:N // 2] for x in board[:N // 2]]
        B = [x[N // 2:] for x in board[:N // 2]]
        C = [x[:N // 2] for x in board[N // 2:]]
        D = [x[N // 2:] for x in board[N // 2:]]

        dom(A), dom(B), dom(C), dom(D)

dom(board)
print(one)
print(zero)