import sys
sys.stdin = open("input.txt", "rt")
Y, X = map(int, input().split())

board = [input() for _ in range(Y)]

for i in range(Y-7, X-7):
    
print(board[0][0:8])
print(board[1][0:8])
print(board[2][0:8])
print(board[3][0:8])
print(board[4][0:8])
print(board[5][0:8])
print(board[6][0:8])
print(board[7][0:8])

