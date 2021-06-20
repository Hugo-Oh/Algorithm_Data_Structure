import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [tuple(map(int, input().split())) for _ in range(N)]


#완전탐색으로 재귀구하는법
#부분구하기
#dp[n] = 시간이[n]일때의 최댓값? X, n번째를 처음 시작 인덱스로 골랐을 때 점수의 최댓값으로 정의하자.
#여기에 시간제한이라는게 심지어 있다!
#dp[n] = d[n-1]

res = 0
def DFS(L, m, tot):
    global res
    if m > M:
        return

    if L == N:
        if tot > res:
            res = tot
        return

    else:
        DFS(L+1, m + arr[L][1], tot + arr[L][0])
        DFS(L+1, m, tot)

DFS(0, 0, 0)
print(res)




#더 큰게 있나? 최대점수를 구하는 것.
