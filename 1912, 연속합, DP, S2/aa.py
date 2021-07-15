import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
#arr = [sum(arr[:n+1]) for n in range(N)] #연속합


for now in range(1, N):
        arr[now] = max(arr[now], arr[now - 1] + arr[now])

print(max(arr))

