import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr =list(map(int, input().split()))

tot = 0

for i in sorted(arr)[::-1]:
    cnt = 0
    for j in arr:
        if j > i:
            cnt += 1
        elif j == i:
            print(cnt, end = " ")
            break


print(cnt)