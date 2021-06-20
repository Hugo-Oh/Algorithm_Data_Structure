import sys
n = int(input())
for _ in range(n):
    N, s, e, k = map(int, input().split())
    arr = list(map(int,input().split()))[s-1 : e]
    arr.sort()
    print(f"#{_+1} {arr[k - 1]}")
