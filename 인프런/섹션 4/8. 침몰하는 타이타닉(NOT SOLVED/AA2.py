import sys
sys.stdin = open("in3.txt", "rt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse = True)
cnt = 0
while arr:
    cnt += 1
    temp = arr.pop(0)

    for i in arr:
        if temp + i <= M:
            arr.remove(i)
            break


print(cnt)



