import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
stack = []
for _ in range(n):
    temp = int(input())
    if stack and temp == 0:
        stack.pop()
    else:
        stack.append(temp)

print(sum(stack))