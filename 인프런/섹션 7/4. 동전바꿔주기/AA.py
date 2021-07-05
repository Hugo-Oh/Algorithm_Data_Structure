import sys
#sys.stdin = open("input.txt", "rt")

M = int(input())
N = int(input())
coin = [list(map(int, input().split())) for _ in range(N)]
coin.sort(key = lambda x : x[0], reverse = True)

cnt = 0
coins = [x[1] for x in coin]
#print(coins)

def DFS(L, tot):
    global cnt
    if tot > M:
        return

    if tot == M:
        cnt += 1
        return

    if L == N:
        return


    else:
        for i in range(coins[L] + 1):
            DFS(L+1, tot + i * coin[L][0])

DFS(0, 0)
print(cnt)