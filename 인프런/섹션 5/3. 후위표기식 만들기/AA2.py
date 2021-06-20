"""import sys
sys.stdin = open("input.txt", "rt")
"""
mid = input()

res = ""
stack = []
#연산자와 피 연산자
#즉 연산자 따로 피 연산자(숫자) 따로

for i in mid:
    if i.isdecimal():
        res += i

    else:
        if i == "(":
            stack.append(i)

        elif i == "*" or i == "/" :
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                res += stack.pop()
            stack.append(i)

        elif i == "+" or i == "-":
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(i)

        elif i == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(res)
