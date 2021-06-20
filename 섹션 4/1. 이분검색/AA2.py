import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

l = 0
r = N - 1

while l <= r:
    mid = (l + r) // 2
    if arr[mid] < M:
        l = mid + 1
    elif arr[mid] > M:
        r = mid - 1
    else:
        print(mid + 1)
        break






