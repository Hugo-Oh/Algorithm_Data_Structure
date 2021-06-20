"""import sys
sys.stdin = open("input.txt", "rt")"""
N = int(input())

res = []
ckr = []

for _ in range(N):
    res.append(input())

for _ in range(N-1):
    ckr.append(input())

while ckr:
    temp = ckr.pop(0)
    if temp in res:
        res.remove(temp)

print(res[0])