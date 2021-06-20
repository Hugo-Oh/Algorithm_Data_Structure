"""import sys

sys.stdin = open("input.txt", "rt")
"""
n, m = map(int, input().split())
arr = list(map(int, input().split()))

def counter(x):
    sum = 0
    cnt = 1
    for i in arr:
        if sum + i > x:
            cnt += 1
            sum = i
        else:
            sum += i
    return cnt

l = 1
r = sum(arr)
res = 0
while l <= r:
    mid = (l + r) // 2
    if counter(mid) <= m:
        res = mid
        r = mid - 1
    else:
        l = mid + 1

print(res)















"""
import sys
sys.stdin=open("input.txt", "r")
def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n, m=map(int, input().split())
Music=list(map(int, input().split()))
maxx=max(Music)
lt=1
rt=sum(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)
"""
# 오름차순 아님.
# 칸막이의 개념으로 가면 어떨까
# DVD m개로 구분하기 위해서는 일단 칸막이의 갯수가 m-1개 필요하다
# m=3라고 치면, 일단 칸막이가 전부다 앞에 있는 경우 arr[0:1] arr[1:2] arr[2:] 이런느낌이 되겠지
# 이 칸막이 내 합 중에서 가장 큰 값을, 기존의 값이랑 비교해서 더 작으면 교체, 칸막이의 범위를 이분검색으로 계속 분할한다면?
# 문제는 칸막이가 여러개라는 것인데....
# 이렇게하면 안될것같기도 하고 그냥 다 돌아버려?
# 재귀로 풀어?

