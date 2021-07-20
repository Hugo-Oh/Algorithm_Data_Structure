import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
ny = [0, 1]
nx = [1, 0]
dp[0][0] = board[0][0]

for now_y in range(N):
    for now_x in range(N):
    
    
    
    
for c in board:
    print(c)