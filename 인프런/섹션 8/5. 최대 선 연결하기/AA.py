import sys
sys.stdin = open("in3.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))

dp1 = [1 for _ in range(N)]
dp2 = [1 for _ in range(N)]
for now in range(1, N):
    max_l = 0
    for before in range(now-1, -1, -1):
        if arr[before] < arr[now] and dp1[before] > max_l:
            max_l = dp1[before]
            #dp1[now] = max(dp1[before] + 1, dp1[now])
    dp1[now] = max_l + 1
            
arr = list(reversed(arr))
"""for now in range(N):
    for before in range(now):
        if arr[before] < arr[now]:
            dp2[now] = max(dp2[before] + 1, dp2[now])"""
#print(dp1)
#print(arr)
#print(dp2)
print(max(dp1))

            
            