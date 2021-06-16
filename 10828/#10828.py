import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

stack = []

for i in range(N):
    a = input()
    if "push" in a:
        num = int(a.split()[1])
        stack.append(num)
    elif "pop" in a:
        if not stack:
            print("-1")
        else:
            print(stack.pop())
    elif "size" in a:
        print(len(stack))

    elif "empty" in a:
        if stack:
            print(0)
        else:
            print(1)

    else:
        if not stack:
            print(-1)

        else:
            print(stack[-1])

import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

stack = []
res = []

for i in range(N):
    a = input()
    if "push" in a:
        num = int(a.split()[1])
        stack.append(num)
    elif "pop" in a:
        if not stack:
            res.append("-1")
        else:
            res.append(stack.pop())
    elif "size" in a:
        res.append(len(stack))

    elif "empty" in a:
        if stack:
            res.append(0)
        else:
            res.append(1)

    else:
        if not stack:
            res.append(-1)

        else:
            res.append(stack[-1])

for i in res:
    print(i)
