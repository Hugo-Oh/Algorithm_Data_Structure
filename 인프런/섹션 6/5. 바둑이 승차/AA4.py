import sys

#sys.stdin = open("in2.txt", "rt")

CAP, N = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))

check = [0] * N
result = -21470000
total = sum(arr)
def DFS(n, tot, max_left):
    global result

    if tot + max_left < result:
        return

    if n == N:
        return

    if CAP > tot + arr[n] > result:
        result = tot + arr[n]

    if tot + arr[n] > CAP:
        return

    DFS(n+1, tot + arr[n], max_left - arr[n])
    DFS(n+1, tot, max_left - arr[n])

DFS(0, 0, total)
print(result)

