N =int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

#1오른쪽
M = int(input())
for _ in range(M):
    n, m, k = map(int, input().split())
    n = n - 1
    if m == 1:
        arr[n] = arr[n][-k:] + arr[n][:-k]
    else:
        arr[n] = arr[n][k:] + arr[n][:k]

l = 0
r = N
tot = 0
for i in range(N):
    for j in range(l, r):
        tot+=arr[i][j]

    if i <= N//2:
        l += 1
        r -= 1
    else:
        l -= 1
        r += 1

print(tot)

