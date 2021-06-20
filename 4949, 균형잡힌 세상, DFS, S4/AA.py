import sys
sys.stdin = open("input.txt", "rt")

res = []
while True:
    n = input()
    if n == ".":
        break

    check = []
    for i in n:
        if i in ["[", "]", "(", ")"]:
            check.append(i)

    stack = []
    for i in check:
        if stack and i == "]" and stack[-1] == "[":
            stack.pop()
        elif stack and i == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(i)

    if stack:
        res.append("no")
    else:
        res.append("yes")

for i in res:
    print(i)

