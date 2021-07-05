from collections import deque
S = "cdcd"
stack=[]
for s in S:
    if stack and s == stack[-1]:
        stack.pop() #안비어져있고 스택의 최신거랑 같으면
    else:
        stack.append(s)
print(stack)
if stack:
    print(0)
else:
    print(1)




