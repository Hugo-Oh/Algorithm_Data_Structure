import sys
import heapq as hq
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
N = int(input())
arr = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if arr:
            #temp = list(map(lambda x : abs(x), arr))
            print(hq.heappop(arr)[1])
        else:
            print(0)
    else:
        hq.heappush(arr, (abs(num), num))