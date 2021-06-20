#import sys
#sys.stdin = open("in3.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))[::-1]
c = int(input())

result = 21470000

def DFS(c, cnt):
    global result
    if c == 0:
        if cnt < result:
            result = cnt
        return

    if c < 0:
        return

    if cnt > result:
        return

    for i in range(N):
        DFS(c - arr[i], cnt + 1)

DFS(c, 0)
print(result)