import sys
sys.stdin = open("in1.txt", "rt")
n, m = map(int, input().split())
cnt = 0
arr = []
for i in range(n):
    arr.append(int(input()))

def checker(len):
    cnt = 0

    for i in arr:

        cnt += i // len

    return cnt

l = 0
r = max(arr) - 1

while l <= r :
    mid = (l + r) // 2
    if checker(mid) < m:
        r = mid - 1
    else:
        l = mid + 1

print(mid)


