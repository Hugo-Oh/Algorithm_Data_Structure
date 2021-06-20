"""import sys
sys.stdin = open("input.txt", "rt")"""

N, M = map(int, input().split())

hut = []
for i in range(N):
    hut.append(int(input()))

hut.sort()

def min_dist(dist):
    sp = hut[0]
    cnt = 1
    for i in hut:
        if i - sp >= dist:
            sp = i
            cnt += 1
    return cnt

l = 0
r = max(hut)

while l <= r:
    mid = (l + r) // 2
    if min_dist(mid) >= M:
        l = mid + 1
        res = mid
    else:
        r = mid - 1

print(res)
