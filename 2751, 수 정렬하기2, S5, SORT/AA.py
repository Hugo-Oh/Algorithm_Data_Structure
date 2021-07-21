import sys
sys.stdin = open("input.txt", "rt")


N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

for a in arr:
    print(a)