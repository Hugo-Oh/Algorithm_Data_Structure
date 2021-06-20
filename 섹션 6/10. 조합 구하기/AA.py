import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
arr = list(range(1, N + 1))
res = [0 for _ in range(M)]
count = 0

def DFS(L, s):
    global count

    if L == M:
        for i in res:
            print(i, end = " ")
        print()
        count += 1
        return

    else:
        for i in range(s, N+1):
            res[L] = i
            DFS(L + 1 , i + 1)


DFS(0, 1)
print(count)



