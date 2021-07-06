sticker = [1, 3, 2, 5, 4]
L = len(sticker)
 #최대값을 구하시오!
 #dp로 구해보는건?
 #dp[i] = max(dp[i-2] + arr[i], dp[i], dp[i-1] #아무것도 안고르는것)
 #i == n인경우에느 dp[0]은 제외시켜야함? 혹은 dp[n] - arr[0]? #원형인 경우..
 #아니면 애초에 DFS로 구해보자. 최적합?
 #DFS(N): = N번쨰 까지 구했을때 최대합

res = -21470000
track = ""
def DFS(N, TOT, st):
    global res, track
    if N >= L:
        if ('0' not in st and f'{L}' not in st):
            if TOT > res:
                res = TOT
                track = st
        return

    else:
        DFS(N+1, TOT, st) #안고르거나, 다음으로 넘기거나,
        DFS(N+2, TOT + sticker[N], st + str(N)) #골랐으면 다음껀 아예 못씀, 다다음꺼에서 선택해야함, 다다음것도 선택하지 않을수 있음. 그건 앞에거.
        #처음과 마지막 고른경우는 제외하자. 어떻게하지..
        #DFS(N+2, TOT)
        #DP N ^ 2

DFS(0, 0, " ")
print(res, track)

#BFS로 풀걸