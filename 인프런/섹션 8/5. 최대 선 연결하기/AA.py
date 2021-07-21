import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

#첫 줄에 겹치지 않고 그을 수 있는 최대선의 갯수!!!!
#-> 증가수열의 갯수를 구하세요
#print(arr)
#dp[i] = i번째 왼쪽을 사용했을떄 (인덱스)얻을 수 있는 최대 선의 ㄱ갯수
#dp[0] = 1?!
dp = [1 for _ in range(n)]
dp[0] = 0

for now in range(n):
    for before in range(now):
        if arr[now] > arr[before]:
            dp[now] = max(dp[now], dp[before] + 1)

print(max(dp))