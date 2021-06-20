import sys
sys.stdin = open("input.txt", "rt")

N, F = map(int, input().split()) # 4, 16

arr = list(range(1, N + 1))

check = [0] * N
res = [0] * N
cnt = 0

def DFS(L, tsum):
    global cnt
    if L == N and tsum == F:
        for i in res:
            print(i, end = " ")
        print()
        sys.exit(0)

    else:
        for i in range(N):
            if check[i] == 0:
                check[i] = 1
                res[L] = arr[i]
                DFS(L+1)
                check[i] = 0

DFS(0)
print(cnt)

# 메트로이드(matriod) 구조
