import sys
sys.stdin=open("input.txt", "rt")

N = int(input())
for _ in range(N):
    a = input()
    stack = []

    #stack
    for i in a:
        if stack and stack[-1] == "(" and i == ")":
            stack.pop()
        else:
            stack.append(i)

    if stack:
        print("NO")
    else:
        print("YES")

