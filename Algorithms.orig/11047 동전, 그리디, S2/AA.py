import sys
sys.stdin = open("input.txt","rt")

N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort(reverse = True)

cnt = 0
i = 0
res = 0
while True:
    if arr[i] <= M:
        res += M // arr[i]
        M = M - (M//arr[i] * arr[i])

    if M == 0 :
        break

    i+=1

print(res)

