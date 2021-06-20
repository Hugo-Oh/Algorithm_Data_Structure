import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

arr = [0] * m
check = [0] * n
def DFS(L):
    global cnt
    if L == m:
        for i in arr:
            print(i, end = " ")
        print()
        cnt += 1
        return

    else:
        for i in range(1, n+1):
            if check[i-1] == 0:
                check[i-1] = 1
                arr[L] = i
                DFS(L + 1)
                check[i-1] = 0
cnt = 0
DFS(0)
print(cnt)