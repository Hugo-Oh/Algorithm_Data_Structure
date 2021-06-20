#import sys
#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))

def count(cap):
    sum = 0
    count = 1
    for i in arr:
        if sum + i <= cap:
            sum = sum + i
        else:
            sum = i
            count += 1

    return count

left = 1
right = sum(arr)

while left <= right:
    mid = (left + right) // 2

    if count(mid) > M:
        left = mid + 1

    else:
        res = mid
        right = mid - 1

print(res)

