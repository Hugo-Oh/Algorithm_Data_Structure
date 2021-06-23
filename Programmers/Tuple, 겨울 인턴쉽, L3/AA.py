s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
#s = s.split(",")
s = s.strip("{|}").split("},{")
s = [list(map(int, x.split(","))) for x in s]

s.sort(key = lambda x : len(x)) #길이 기준으로 정렬


res = []

for group in s:
    for num in group:
        if num not in res:
            res.append(num)

print(res)