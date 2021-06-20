razor = input()

stack = []
tot = 0
for i in range(len(razor)):
    if razor[i] == "(":
        stack.append(i)

    else:razor[i-1] == "(":
            stack.pop()
            tot += len(stack)

        else:
            stack.pop()
            tot += 1
        if



res = tot

print(res)