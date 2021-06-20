

"""n, m = map(int, input().split())
arr = list(map(int, input().split()))
"""
"""
arr = [1, 2, 1, 3, 1, 1, 1, 2]
m = 3

cnt = 0

for i in range(0, len(arr) -1):
    if sum(arr[i:]) > m:
        continue

    for j in range(i, len(arr)):
        if sum(arr[i:j+1]) > m:
            break

        if sum(arr[i:j+1]) == m:
            cnt += 1
            break

print(cnt)"""


n, m = map(int, input().split())
arr = list(map(int, input().split()))

tot = arr[0]
lt = 0
rt = 0
cnt = 0

while True:
    if tot == m:
        tot -= arr[lt]
        lt += 1
        cnt += 1
    elif tot < m:
        if rt < n-1:
            rt += 1
            tot += arr[rt]
        else:
            break
    elif tot > m:
        tot -= arr[lt]
        lt += 1

print(cnt)