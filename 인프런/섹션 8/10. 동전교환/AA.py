import sys
#sys.stdin = open("input.txt", "rt")

N =int(input())
coin = list(map(int, input().split()))
tot_change = int(input())
#dp[i] = 5원을 거슬러주기 위해 필요한 최소 코인의 갯수
dp = [1000 for _ in range(tot_change+1)]
dp[0] = 0 #0원은 없어도 되니까 ㅎ
for coin_v in coin:
    for now_c in range(1, tot_change+1):
        dp[now_c] = min(dp[now_c], dp[now_c - coin_v] + 1)

print(dp[tot_change])
