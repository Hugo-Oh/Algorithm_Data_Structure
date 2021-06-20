import sys
#sys.stdin=open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
c = 0
check = [0] * N
def DFS(n, c):
    if c > n//2:
        return

    if n == N:
        tot_c = 0
        for i in range(n):
            if check[i] == 1:
                tot_c += arr[i]

        if tot_c == total - tot_c:
            print("YES")
            sys.exit()

        return

    else:
        check[n] = 1
        DFS(n+1, c+1)
        check[n] = 0
        DFS(n+1, c)

if DFS(0, 0) == "YES":
    print("YES")
else:
    print("NO")