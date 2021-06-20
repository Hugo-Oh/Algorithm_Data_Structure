import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
arr = []

arr = list(map(int, input().split()))
arr.sort()

left = 0
right = N - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] > M:
        right = mid - 1

    elif arr[mid] < M:
        left = mid + 1

    else:
        print(mid + 1)
        break
