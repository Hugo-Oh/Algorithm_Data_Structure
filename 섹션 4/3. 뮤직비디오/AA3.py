"""import sys

sys.stdin = open("in1.txt", "rt")
"""
n, m = map(int, input().split())
arr = list(map(int, input().split()))

def counter(capa):
    sum = 0
    cnt = 1
    for i in arr:
        if sum + i > capa:
            sum = i
            cnt += 1
        else:
            sum += i

    return cnt

l = 0
r = sum(arr) - 1

while l <= r:
    mid = (l + r) // 2
    if counter(mid) > m:
        l = mid + 1
    else:
        res = mid
        r = mid - 1

print(res)
