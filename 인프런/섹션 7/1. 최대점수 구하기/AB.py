import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x : (x[1]), reverse = True)
#print(arr)

#dp[i] = i일차를 한다고 했을때에 할 수 있는 최대값, 소요시간
#dp[i][1] = dp[i] + dp[i] #제한조건 1
#dp[i][0] = max(dp[i-1][0] + arr[i][0], dp[i][0])
dp = [[0, 0] for _ in range(N)]
dp[0] = arr[0]
for now in range(N):
    for past in range(now):
        if dp[past][1] + arr[now][1] <= M: #완전탐색하고싶은데 왜이럴까 #dp[i][0] = 최대점수, 그때 걸리는 시간
            dp[now][0] = max(dp[past][0] + arr[now][0], dp[now][0], arr[past][0] + arr[now][0])
            if max(dp[past][0] + arr[now][0], dp[now][0], arr[past][0] + arr[now][0]) == dp[past][0] + arr[now][0]:
                dp[now][1] = dp[past][1] + arr[now][1]
            elif max(dp[past][0] + arr[now][0], dp[now][0], arr[past][0] + arr[now][0]) == dp[now][1]:
                dp[now][1] = arr[past][1] + arr[now][1]




print(arr)
print(dp)


