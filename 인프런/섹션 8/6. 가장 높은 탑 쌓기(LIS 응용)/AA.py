import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

graph = [tuple(map(int, input().split())) for _ in range(N)]
#dp[i] = i번째 인덱스 사용했을때 얻을 수 있는 높이의 최대값
dp = [0 for _ in range(N)]
graph.sort(key = lambda x : x[0], reverse = True)

for now in range(N):
    dp[now] = graph[now][2]
    for before in range(now):
        if graph[now][2] > graph[before][2]:
            dp[now] = max(dp[now], dp[before] + graph[now][1])

print(max(dp))