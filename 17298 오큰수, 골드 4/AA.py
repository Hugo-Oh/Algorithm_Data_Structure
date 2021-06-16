import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))

stack = [arr[0]] # 1 <= N이므로
res = []

for i in arr:
    if stack[-1] > i:
        res.append(i)

    else:
        stack[-1] = i
        res.append(i)

print(res)