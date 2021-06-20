"""import sys
sys.stdin = open("input.txt", "rt")
"""
n = list(map(str,input()))

#1. 숫자면 그냥 담기
#2.
#3.
#4.
stack = []
for i in n:
    if i.isdecimal():
        stack.append(i)

    else:

        if i == "(":
            stack.append(int(i))

        elif i == "+" :
            stack.append(int(stack.pop()) + int(stack.pop()))

        elif i == "-" :
            stack.append(-int(stack.pop()) + int(stack.pop()))

        elif i == "*" :
            stack.append(int(stack.pop()) * int(stack.pop()))

        elif i == "/" :
            stack.append(int(stack.pop()) / int(stack.pop()))


print(stack[0])