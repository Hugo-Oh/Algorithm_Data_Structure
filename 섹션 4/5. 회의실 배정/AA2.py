"""import sys
sys.stdin = open("input.txt", "rt")
"""

N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x : (x[1], x[0]))

et = 0
cnt = 0
for start, end in arr:
    if start >= et:
        cnt += 1
        et = end

print(cnt)

