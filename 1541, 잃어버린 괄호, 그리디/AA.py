import sys

sys.stdin = open("input.txt", "rt")

a = input().split("-")
res = 0
for i in a[0].split("+"):
    res += int(i)

for i in a[1:]:
    for j in i.split("+"):
        res -= int(j)

print(res)




# 55 라고 치면, 5 + 5 or 5 -5 두가지의 선택지가 있다.
# 이 값을 더하거나, 아무것도 아닐때는(+라고 치자) 이 값이 작을수록 좋고,
# 이 값이 빼지면 이 값이 클수록 좋다(아무것도 손대지 않는다)




