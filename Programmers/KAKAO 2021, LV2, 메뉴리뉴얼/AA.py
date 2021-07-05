import re
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
orders = ["".join(sorted(x)) for x in orders]
course = [2,3,4]
result = ["AC", "ACDE", "BCFG", "CDE"]


menu = []
menu = "".join(orders) #일단 다 합치고
menu = sorted(list(set(menu))) #셋으로 중독 제거 후 다시 리스트화

#1번방법 단순완전탐색(재귀 X..하려했는데 2 ~ 10이면 너무 많음)
#2번방법 라이브러리 쓰기
from itertools import combinations #이걸 def로 나중에 해보자

res = []

for number in course:
    comb = combinations(menu, number)

    for com in comb:
        cnt = 0
        check = "".join(com)
        for order in orders:
            if check in order:
                print(check, order)
                cnt += 1

        if cnt > 1:
            print(check)
            res.append(check)

print(res)