import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
for _ in range(N):
    n = input()
    stack = []
    for i in n:
        if stack and i == ")" and "(" in stack:
            stack.pop()

        else:
            stack.append(i)

    if stack:
        print("NO")
    else:
        print("YES")
