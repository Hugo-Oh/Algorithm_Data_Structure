"""import sys
sys.stdin = open("input.txt", "rt")"""

L = int(input())
arr = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    high = -100000
    low = 100000
    idx_high = 0
    idx_low = 0

    for i, v in enumerate(arr):

        if v > high:
            high = v
            idx_high = i

        if v < low:
            low = v
            idx_low = i

    arr[idx_high] -= 1
    arr[idx_low] += 1

Maxx = max(arr)
Minn = min(arr)

print(Maxx - Minn)


