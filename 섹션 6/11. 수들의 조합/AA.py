import sys
sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
arr = list(map(int,input().split()))
M = int(input())

res = [0] * (K+1)
count = 0

def DFS(L, s, sum):
    global count

    if L == K and not sum % M :
        count += 1

        print(L, sum)
        print(res[:-1])
        return

    if L > K:
        return

    else:
        for i in range(s, N):
            res[L] = arr[i]
            DFS(L + 1, i + 1, sum + arr[i])

DFS(0, 0, 0)

print(count)