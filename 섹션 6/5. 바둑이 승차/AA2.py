import sys
sys.stdin = open("input.txt", "rt")

CAP, N = map(int, input().split())

arr = []
check = [0] * (N)

for _ in range(N):
    arr.append(int(input()))


result = -2147000000
def DFS(n, tot):
    if n == N:
        result = tot

    else:
        check[n] = 1
        DFS(n+1)
        check[n] = 0
        DFS(n+1)

res = []
DFS(1)

print(max(res))