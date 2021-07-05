import sys
from _collections import deque
#sys.stdin = open("input.txt", "rt")

n = int(input())

deq = deque(list(range(1, n+1)))

while len(deq) > 1 :
    deq.popleft()
    deq.append(deq.popleft())

print(deq[0])