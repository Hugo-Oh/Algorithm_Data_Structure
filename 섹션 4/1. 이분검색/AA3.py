"""import sys
sys.stdin = open("input.txt", "rt")
"""

"""import sys
sys.stdin=open("input.txt", "r")
n, m=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
lt=0
rt=n-1
while lt<=rt:
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1"""
n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

l = 0
r = n

while True:
    mid = (l + r) // 2
    if l == r:
        break

    if arr[mid] == k:
        print(mid + 1)
        break

    elif arr[mid] < k:
        l = mid

    else:
        r = mid