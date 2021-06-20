#import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
res = [0] * N

for n in range(1, N+1):
    k = arr[n-1]
    i = 0
    cnt = 0
    while True:
        if cnt == k:
            while res[i] != 0 and i + 1 < N:
                i += 1
            res[i] = n
            break

        if res[i] == 0:
            cnt += 1
            i += 1
        else:
            i += 1

for i in res:
    print(i, end = " ")










