import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
N =int(input())

arr = [0] * 10001

for _ in range(N):
    arr[int(input())] += 1

for i in range(N):
    if arr[i] != 0:
        for k in range(arr[i]):
            sys.stdout.write(f"{i}" + '\n')