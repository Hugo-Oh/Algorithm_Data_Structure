key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


M = 3

check = []
check_rot = []
for y in range(M):
    for x in range(M):
        if key[y][x] == 1:
            check.append((y, x))

N = 3
target = []
for y in range(N):
    for x in range(N):
        if lock[y][x] == 0:
            target.append((y, x))


print(target)
print(check)

for i in key:
    print(i)
key = [[key[j][i] for j in range(M -1, -1, -1)] for i in range(M)]
for y in range(M):
    for x in range(M):
        if key[y][x] == 1:
            check_rot.append((y, x))
print()
for i in key:
    print(i)
key = [[key[j][i] for j in range(M -1, -1, -1)] for i in range(M)]
print()
for i in key:
    print(i)
target = [(), ()]
key = 3
print(target)
print(check)
print(check_rot)

#print(rot)
#1 check를 기준으로 90도 회전해보

"""2, 1 -> 1, 0
2, 2 -> 2, 0
1, 0 -> 0, 1
print(target)"""
