"""import sys
sys.stdin = open("input.txt", "rt")
"""

key = input()
value = input()

p_1 = dict()
p_2 = dict()

for i in key:
    if i in p_1:
        p_1[i] += 1
    else:
        p_1[i] = 1

for j in value:
    if j in p_2:
        p_2[j] += 1
    else:
        p_2[j] = 1

if p_1 == p_2:
    print("YES")
else:
    print("NO")


