import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = []
for i in range(N):
    arr.append(tuple(map(int, input().split())))


