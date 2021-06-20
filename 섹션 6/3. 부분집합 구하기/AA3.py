import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = [0] * (N+1)
def dfs(n):
    if n == N + 1:
        for i in range(1, N+1):
            if arr[i] == 1:
                print(i, end = " ")
        print()
    else:
        arr[n] = 1 #사용한다
        dfs(n+1)

        arr[n] = 0 #사용하지 않는다
        dfs(n+1)

dfs(1)


"""
def DFS(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1
        DFS(v + 1)
        ch[v] = 0
        DFS(v + 1)


if __name__ == "__main__":
   n = int(input())
    ch = [0] * (n + 1)
    DFS(1)"""


