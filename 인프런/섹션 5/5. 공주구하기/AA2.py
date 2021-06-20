"""import sys
sys.stdin = open("input.txt", "rt")
"""
N, K = map(int, input().split())
#N, K = 20, 3
arr = list(range(1, N+1))
cnt = 0
"""1 2 4 5 6 7 8 [다음꺼]
1 2 5 6 7 8 [다음꺼]
#1. remove + index로 제거하는 방법이 있지만 사용 안할꺼
#2. queue 로 쌓아보자.


cnt = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8]
"""

while len(arr) > 1:
    for i in arr:
        cnt += 1
        if cnt == K:
            arr.remove(i)
            arr = arr[K - 1:] + arr[ : K - 1]
            cnt = 0
            break

print(arr[0])



