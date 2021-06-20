import sys
sys.stdin = open("in2.txt", "rt")

n, m = map(int, input().split())

n = list(map(int, str(n)))

stack = []
for i in n:
    while stack and stack[-1] < i and m > 0:
        stack.pop()
        m -= 1

    stack.append(i)

if m!=0:
    stack=stack[:-m]

stack = "".join(map(str, stack))
print(stack)

