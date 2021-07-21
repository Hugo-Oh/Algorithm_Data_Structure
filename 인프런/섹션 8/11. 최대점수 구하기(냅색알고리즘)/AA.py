import sys
#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
<<<<<<< HEAD

arr = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(M+1)] #dp[i] = i초일때 얻을 수 있는 최대 스코어
for s, t in arr:
    for tot_s in range(M, t-1, -1):
        dp[tot_s] = max(dp[tot_s], dp[tot_s - t] + s)

print(dp[M])



=======
#dp[i] = 제한시간 i초일때 얻을수 있는 최대 스코어
# but 한번만 사용할수 있음, 이차원 그래프를 사용 할 수도 있고, 아닐수도 있다! 뿌슝빠슝
dp = [0 for _ in range(M+1)]
dp[0] = 0 #0초일때는 0점.
#
# for _ in range(N):
#     score, time = map(int, input().split())
#     for cur_t in range(time, M+1):
#         dp[cur_t] = max(dp[cur_t], dp[cur_t - time] + score)
#

# print(dp)
#이 정답은 안된다. 왜냐하면 이전에 사용했던 기록이 또 사용된다 = 중복이 허용된다
#즉 2차원 그래프를 통해서 그걸 없애거나, 혹은 이전의 기록을 사용하지 않게 역순으로!
for _ in range(N):
    score, time = map(int, input().split())
    for cur_t in range(M, time-1, -1):
        dp[cur_t] = max(dp[cur_t], dp[cur_t - time] + score)

print(dp[M])
>>>>>>> 12f586e6b02d24679e5a3438eed3e6f0e609487b
