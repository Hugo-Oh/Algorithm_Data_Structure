#import sys
#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

arr = list(range(1, N+1))
k = 1
while True:
    if k == M:
        arr.pop(0)
        k = 1

    if len(arr) == 1:
        print(arr[0])
        break

    a = arr.pop(0)
    arr.append(a)
    k = k + 1







