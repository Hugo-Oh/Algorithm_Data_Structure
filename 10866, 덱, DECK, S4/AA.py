import sys
from _collections import deque

sys.stdin = open("input.txt", "rt")
#input = sys.stdin.readline


def push_back(n):
    queue.append(n)

def push_front(n):
    queue.appendleft(n)

def pop_back():
    if queue:
        print(queue.pop())
    else:
        print(-1)
def pop_front():
    if queue:
        print(queue.popleft())
    else:
        print(-1)

def front():
    if queue:
        print(queue[0])
    else:
        print(-1)

def back():
    if queue:
        print(queue[-1])
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    if queue:
        print(0)
    else:
        print(1)

queue = deque()
N = int(input())

for _ in range(N):
    inp = input()

    if inp == "front":
        front()

    elif inp == "back":
        back()

    elif inp == "size":
        size()

    elif inp == "empty":
        empty()

    elif inp == "pop_front":
        pop_front()

    elif inp == "pop_back":
        pop_back()

    else:
        inp = inp.split()
        if inp[0] == "push_front":
            push_front(int(inp[1]))

        else:
            push_back(int(inp[1]))

