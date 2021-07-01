import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp_1 = [1 for _ in range(n)]
dp_2 = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_1[i] = max(dp_1[i], dp_1[j] + 1)

arr = list(reversed(arr))

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_2[i] = max(dp_2[i], dp_2[j] + 1)
dp_2 = list(reversed(dp_2))


dp_3 = [x + y -1 for x, y in zip(dp_1, dp_2)]
# print(arr)
# print(dp_1)
# print(dp_2)
print(max(dp_3))
