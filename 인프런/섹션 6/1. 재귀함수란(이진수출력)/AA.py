"""import sys
sys.stdin = open("input.txt", "rt")
"""
n = int(input())

def DFS(n):
    if n // 2 < 1:
        print(n % 2, end = "")
        return
    DFS(n // 2)
    print(n % 2, end="")


DFS(n)