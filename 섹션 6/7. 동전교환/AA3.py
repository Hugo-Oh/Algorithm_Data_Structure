"""import sys
sys.stdin = open("input.txt", "rt")
"""

N = int(input())
kind = list(map(int, input().split()))[::-1]
change = int(input())
arr = [0] * N

min_count = 21470000
def DFS(n, arr, change):
    global min_count
    if change == 0 and min_count:
        min_count = sum(arr)
        return n

    if change < 0:
        return

    for i in range(N):
        DFS(n+1, arr, change - kind[i] * arr[i])
        arr[i] += 1

DFS(0, arr, change)
print(min_count + 1)