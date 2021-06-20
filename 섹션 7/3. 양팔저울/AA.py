import sys
sys.stdin = open("input.txt", "rt")

N =int(input())
arr = list(map(int, input().split()))

weight = [0] * N
sum_left = []
def DFS(L, left, right, resid):
    if L == N:
        return
    else:
        DFS(L+1, left + arr[L], right, resid)
        DFS(L+1, left, right + arr[L])
        DFS(L+1, left, right, resid + arr[L])
DFS(0, 0)
S = sum(arr)
print(S)
cnt = 0
for s in range(1, S+1):
    if s in sum_left:
        pass

print(sum_left) #추로 표현할수 있는 무게
s = 1
sum_left = [x + s for x in sum_left] # s + 추로 표현할 수 있는 무게
print(sum_left)

