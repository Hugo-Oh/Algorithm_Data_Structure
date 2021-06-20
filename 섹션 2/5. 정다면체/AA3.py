n, m = map(int, input().split())

dic = dict()
for i in range(1, n+1):
    for j in range(1, m+1):
        total = i+j
        if total in dic:
            dic[total] += 1
        else:
            dic[total] = 1
max_std = max(dic.values())
for key, value in dic.items():
    if max_std == value:
        print(key, end = " ")
