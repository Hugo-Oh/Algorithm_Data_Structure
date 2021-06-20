import math


A = sorted([5, 1, 3, 7])
B = sorted([2, 2, 6, 8])
print(A, B)
sum = 0
print(round(1,2))


round()
for i in B: #이길거면 아슬아슬하개 이기고
    if i > A[0]:
        sum += 1
        A.pop(0)
    else: #질거면 마지막놈한테 붙어서 지자
        A.pop()

print(sum)