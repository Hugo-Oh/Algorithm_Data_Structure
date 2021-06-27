from _collections import deque

queue = deque()
queue.append((1, 2))

x, y = queue.popleft()
print(queue)

print(x, y)
