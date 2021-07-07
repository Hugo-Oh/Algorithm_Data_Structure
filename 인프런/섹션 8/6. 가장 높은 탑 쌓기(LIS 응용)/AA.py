import sys
sys.stdin = open("in4.txt", "rt")

N = int(input())
stones =[tuple(map(int, input().split())) for _ in range(N)]
stones.sort(key = lambda x : x[0], reverse = True)

dp = [0 for _ in range(N)] #높이
dp[0] = stones[0][1]
res = 0
for now in range(1, N):
    max_h = 0
    for before in range(now-1, -1, -1):
        if stones[before][2] > stones[now][2] and dp[before] > max_h: #탑위에 이번껄 올릴 수 있다면
            max_h = dp[before]
        dp[now] = max_h + stones[now][1]
#dp[now] = max(dp[before] + stones[now][1], dp[now])
            
"""and dp[before] > max_h: #탑위에 이번껄 올릴 수 있다면
            max_h = dp[before]
        dp[now] = max_h + stones[now][1]"""
print(dp)
print(max(dp))


#dp[now] = max(dp[before] + stones[now][1], dp[now])
# dp[now] = dp[before] + stones[now][1]) #최대 높이는 새로 쌓은 탑이거나, 아니면 그냥 유지
#print(stones)
#print(dp)
