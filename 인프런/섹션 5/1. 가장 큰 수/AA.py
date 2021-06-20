import sys
#sys.stdin = open("in2.txt", "rt")

n, m = input().split()
stacked = list(map(int, n))

res = []
cnt = 0

for i in stacked:
    while res and cnt < int(m) and i > res[-1] :
        res.pop()
        cnt += 1

    res.append(i)

if cnt != int(m):
    res = res[:-int(m)]

res = "".join(map(str,res))
print(res)













