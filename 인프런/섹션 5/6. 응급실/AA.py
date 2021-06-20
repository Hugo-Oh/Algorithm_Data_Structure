import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
arr = [(x, y) for x, y in enumerate(list(map(int, input().split())))]

k = 0
while arr:
    a = arr.pop(0)
    if any(a[1] < x[1] for x in arr):
        arr.append(a)

    else:
        k += 1
        if a[0] == M:
            break

print(k)






