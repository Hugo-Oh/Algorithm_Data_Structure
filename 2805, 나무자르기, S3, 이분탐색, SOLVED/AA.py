import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
tot = 0

def left(height):
    tmp = sum([x - height for x in arr if x >= height])
    return tmp

l = 0
r = max(arr)
res = -21470000

while l <= r:
    mid = (l + r) // 2
    if left(mid) < M:
        r = mid - 1

    else:
        res = mid
        l = mid + 1

print(res)