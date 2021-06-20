import sys
sys.stdin = open("input.txt", "rt")

L = int(input())
arr = list(map(int, input().split()))
M = int(input())
#한번할때 값

maxx = max(arr)
minn = min(arr)
res = maxx - minn
print(res)
print(sorted(arr))
for i in range(M):
    first = 2
    maxx = maxx - 1
    minn = minn - 1
    res = res - first

print(res)




