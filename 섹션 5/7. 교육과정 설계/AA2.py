"""import sys
sys.stdin = open("input.txt", "rt")
"""

order = input()
N = int(input())

for _ in range(N):
    str = list(input())
    queue = str.copy()

    for i in queue:
        temp = str.pop(0)

        if temp in order:
            str.append(temp)

    res = ""

    for i in str:
        if i not in res:
            res += i

    if res == order:
        print(f"#{_+1} YES")

    else:
        print(f"#{_+1} NO")
