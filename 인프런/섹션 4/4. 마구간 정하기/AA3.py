"""import sys
sys.stdin = open("in2.txt", "rt")"""

N, m = map(int, input().split())
arr = []
for n in range(1, N+1):
    arr.append(int(input()))

arr.sort()

def count(dis):
    sp = arr[0]
    cnt = 1
    for i in range(N):
        if arr[i] - sp >= dis:
            sp = arr[i]
            cnt += 1

    return cnt

l = 1
r = arr[N - 1]

while l <= r :
    mid = (l+r) // 2
    if count(mid) >= m :
        res = mid
        l = mid + 1

    else:
        r = mid - 1

print(res)