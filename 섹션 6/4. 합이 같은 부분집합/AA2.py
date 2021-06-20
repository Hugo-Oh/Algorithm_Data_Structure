import sys
sys.stdin=open("in4.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

check = [0] * (N+1)
res = []
def DFS(n) :
    if n == N + 1:
        tot = 0
        for i in range(1, N+1):
            if check[i] == 1:
                tot += arr[i]
        if tot:
            res.append(tot)

    else:
        if not all(check):
            check[n] = 1 # n 이 있음(0)
            DFS(n+1)

            check[n] = 0 # n 이 없음(x)
            DFS(n+1)

DFS(1)
if len(res) == len(set(res)):
    print("NO")
else:
    print("YES")

print(sorted(res))

#^^ㅑㅇ
