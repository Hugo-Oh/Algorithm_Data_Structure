import sys
sys.stdin = open("input.txt", "rt")

n = input()

stack = []
res = []

for i in range(len(n)):
    if n[i].isnumeric():
        res.append(n[i])

    elif n[i] in ("+", "-"):
        stack.append(n[i])

