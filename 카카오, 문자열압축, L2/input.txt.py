a = "abcabcdede"

n = 3
stack = []
res = ""
for i in range(len(a) // n + 1):
    if stack and stack[-1] == a[i*n:(i+1)*n]:
        stack.append(a[i*n:(i+1)*n])
    elif stack and stack[-1] != a[i*n:(i+1)*n] and len(stack) > 1:
        res += f"{len(stack)}{stack[-1]}"
        stack = []
        stack.append(a[i*n:(i+1)*n])
    else:
        stack.append(a[i*n:(i+1)*n])

if stack:
    res += f"{''.join(stack)}"

print(res)