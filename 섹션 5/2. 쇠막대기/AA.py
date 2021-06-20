#import sys
#sys.stdin = open("input.txt", "rt")

n = list(input())

stack = []
sum = 0

for i in range(len(n)):
    if n[i] == "(":
        stack.append(i)

    else:
        if n[i-1] == "(" and n[i] == ")":
            stack.pop()
            sum += len(stack)

        else:
            stack.pop()
            sum += 1


print(sum)