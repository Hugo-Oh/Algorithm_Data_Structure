from collections import deque
import sys

sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse = True)

dp = [0 for _ in range(k+1)]
dp[0] = 1
for now in arr:
    for next in range(now, k+1):
        if next - now >= 0:
            dp[next] += dp[next - now]

print(dp[k])

# 10
# 10 5 0
# 경우의 수를 출력하시오
# 1. 완전탐색을 생각해보자
# 2. 0이 되는 경우의 수?
# 3.

#DP의 조건 =
#dp는 무한으로 발산하는가?X