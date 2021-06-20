import sys
sys.stdin = open("input.txt", "rt")

N, x = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))
arr.sort()

def count_d(cap):
    global x
    cnt = 1
    loc = arr[0]

    for i in arr[1:]:
        if i - loc >= cap:
            cnt +=1
            loc = i

    return cnt

l = 0
r = max(arr)

res = -2147000
while l <= r:
    mid = (l + r) // 2

    if count_d(mid) >= x:
        res = mid
        l = mid + 1

    else:
        r = mid - 1

print(res)