from _collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque(list(range(1, N+1)))
rule = K
res = []
start = 1

while queue:
    kind = queue.popleft()

    if start == rule:
        res.append(kind)
        start = 1
    else:
        queue.append(kind)
        start += 1

print("<" + ", ".join(map(str, res)) + ">")
