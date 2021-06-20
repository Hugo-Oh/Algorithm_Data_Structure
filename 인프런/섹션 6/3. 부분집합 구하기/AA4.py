"""import sys
sys.stdin = open("input.txt", "rt")
"""
N = int(input())
#arr = list(map(int, input().split()))

check = [0] * N
def DFS(n):
    if n == (N):
        for i in range(0, n):
            if check[i] == 1:
                print(i+1, end = " ")
        print()

    else:
        check[n] = 1
        DFS(n+1)
        check[n] = 0
        DFS(n+1)

DFS(0)