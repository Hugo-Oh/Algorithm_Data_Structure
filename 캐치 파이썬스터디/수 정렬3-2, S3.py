import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
check = [0] * 10001
res = []
for _ in range(n):
    num = int(sys.stdin.readline())
    check[num] = check[num] + 1

for i in range(10001):
    if check[i] != 0:
        for _ in range(check[i]):
            res.append(i)

for i in res:
    print(i)

