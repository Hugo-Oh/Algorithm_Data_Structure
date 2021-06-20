import sys
from collections import deque

#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readlines
N = int(input())

deq = deque()

for _ in range(N):
    n = input()

    if "push" in n:
        deq.append(n.split()[1])

    elif n == "pop":
        if not deq:
            print(-1)
        else:
            tmp = deq.popleft()
            print(tmp)

    elif n == "size":
        print(len(deq))

    elif n == "empty":
        if deq:
            print(0)
        else:
            print(1)

    elif n == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)

    elif n == "back":
        if deq:
            print(deq[-1])
        else:
            print(-1)