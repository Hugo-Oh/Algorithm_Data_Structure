import sys
from collections import deque

def push(my_queue, x):
    my_queue.append(x)

def pop(my_queue):
    if (len(my_queue) == 0): return -1
    elem = my_queue[0]
    my_queue.popleft()
    return elem

def size(my_queue):
    return len(my_queue)

def empty(my_queue):
    if (len(my_queue) == 0): return 1
    else: return 0

def front(my_queue):
    if (len(my_queue) == 0): return -1
    return (my_queue[0])

def back(my_queue):
    if (len(my_queue) == 0): return -1
    return (my_queue[-1])

my_queue = deque([])
num = int(sys.stdin.readline())
for i in range(num):
    command = sys.stdin.readline().split()
    if (command[0] == "pop"): print(pop(my_queue))
    elif (command[0] == "size"): print(size(my_queue))
    elif (command[0] == "empty"): print(empty(my_queue))
    elif (command[0] == "front"): print(front(my_queue))
    elif (command[0] == "back"): print(back(my_queue))
    else: push(my_queue, int(command[1]))