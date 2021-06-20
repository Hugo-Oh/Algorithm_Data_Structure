import sys
sys.stdin = open("in1.txt", "rt")

N, M = map(int, input().split())

arr =  [0] * (N + M + 1)

for i in range(1, N+1):
    for j in range(1, M+1):
        arr[i+j] += 1

maxx = max(arr)

for i, j in enumerate(arr):
    if maxx == j:
        print(i, end = " ")



