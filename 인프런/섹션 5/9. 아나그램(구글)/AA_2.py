import sys
sys.stdin = open("input.txt", "rt")


key = input()
value = input()

p_1 = dict()


for i in key:
    p_1[i] = p_1.get(i, 0) + 1

for j in value:
    p_1[j] = p_1.get(j, 0) - 1
print(p_1.values())
if not all(p_1.values()):
    print("Yes")
else:
    print("NO")