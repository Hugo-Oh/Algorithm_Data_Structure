"""
arr =[
    [0,0,0,0,0,0,0],
    [0,5,3,7,2,3,0],
    [0,3,7,1,6,1,0],
    [0,7,2,5,3,4,0],
    [0,4,3,6,4,1,0],
    [0,8,7,3,5,2,0],
    [0,0,0,0,0,0,0]]
N=5"""
"""
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)
"""

N = int(input())
arr = [[0] * (N+2) for i in range((N+2))]
for i in range(1, N+1):
    arr[i][1:N+1] = list(map(int, input().split()))
cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if arr[i][j] > arr[i+1][j] and arr[i][j] > arr[i][j+1] and arr[i][j] > arr[i-1][j] and arr[i][j] > arr[i][j-1]:
            cnt +=1

print(cnt)

#print(arr)

