"""import sys
sys.stdin = open("input.txt", "rt")"""

CAP, N = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(int(input()))
sum1 = sum(arr)

def DFS(n, tot, tsum):
    global result
    if tot + (sum1 - tsum) < result:
        return

    if tot > CAP:
        return

    if n == N:
        if tot > result:
            result = tot

    else:
        DFS(n+1, tot + arr[n], tot + arr[n])
        DFS(n+1, tot, tot + arr[n])

result = -21470000

DFS(0, 0, 0)

print(result)


