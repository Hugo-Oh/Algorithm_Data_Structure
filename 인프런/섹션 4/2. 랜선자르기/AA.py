import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

def count(n):
    res = [x//n for x in arr]
    res = sum(res)
    return res

left = 1
right = max(arr)

while left <= right:
    mid = (left + right) // 2
    if count(mid) >= M:
        left = mid + 1
        res = mid
    else:
        right = mid - 1

print(res)

