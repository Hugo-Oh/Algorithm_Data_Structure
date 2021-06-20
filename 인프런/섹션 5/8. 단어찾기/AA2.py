"""import sys
sys.stdin = open("input.txt", "rt")
"""
p = dict()
N = int(input())
for _ in range(N):
    p[input()] = 0

for _ in range(N-1):
    p[input()] = 1

for i, j in p.items():
    if j == 0:
        print(i)

