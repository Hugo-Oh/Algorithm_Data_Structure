import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
checker = [0] * N
tot = sum(arr)
ans = False

def DFS(L):
    if L == N:
        result = 0
        for i in range(N):
            if checker[i] == 1:
                result += arr[i]

        if result == tot - result:
            print("YES")
            sys.exit()
    else:
        checker[L] = 1
        DFS(L+1)
        checker[L] = 0
        DFS(L + 1)

DFS(0)
print("NO")