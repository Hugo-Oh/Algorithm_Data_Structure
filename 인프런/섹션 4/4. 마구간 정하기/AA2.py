import sys
sys.stdin = open("input.txt", "rt")

N, m = map(int, input().split())
arr = []
for n in range(1, N+1):
    arr.append(int(input()))

print(sorted(arr))

l = 0
r = N


"""import sys
sys.stdin=open("input.txt", "r")
def Count(len):
    cnt=1
    ep=Line[0]
    for i in range(1, n):
        if Line[i]-ep>=len:
            cnt+=1
            ep=Line[i]
    return cnt

n, c=map(int, input().split())
Line=[]
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()

l = 1
r = arr[n-1]
while l <= r:
    mid = (l + r) // 2
    if Count(mid) >= 
    
def Count(len):
    first = arr[0]
    cnt = 1
    for i in range(1, n):
lt=1
rt=Line[n-1]

while lt<=rt:)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
    mid=(lt+rt

print(res)"""
