

"""N=7
tot = 0
arr = [[10, 13, 10, 12, 15, 1, 2],
[12, 39, 30, 23, 11, 1, 2],
[11, 25, 50, 53, 15, 3, 4],
[19, 27, 29, 37, 27, 5, 6],
[19, 13, 30, 13, 19, 8, 7],
[19, 13, 30, 13, 19, 5, 3],
[19, 13, 30, 13, 19, 3, 7]]
N=5
arr = [
[10, 13, 10, 12, 15],
[12, 39, 30, 23, 11],
[11, 25, 50, 53, 15],
[19, 27, 29, 37, 27],
[19, 13, 30, 13, 19]
]
"""

"""
import sys
sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
res=0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)
"""

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

l = r = N//2
tot = 0
for i in range(N):
    for j in range(l, r+1):
        tot += arr[i][j]
    if i < N//2:
        l -= 1
        r += 1
    else:
        l += 1
        r -= 1

print(tot)


