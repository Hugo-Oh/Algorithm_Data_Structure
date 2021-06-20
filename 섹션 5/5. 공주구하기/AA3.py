"""import sys

sys.stdin = open("input.txt", "rt")
"""
N, K = map(int, input().split())

arr = list(range(1, N+1))
cnt = 0

while len(arr) > 1:
    for i in arr:
        cnt += 1
        if cnt == K:
            cnt = 0
            arr.pop(0)
            break
        else:
            arr.append(arr.pop(0))

print(arr[0])



