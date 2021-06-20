

S = input()
num = ""

for s in S:
    if ord("0") <= ord(s) <= ord("9"):
        num += s

num = int(num)
cnt = 0
for i in range(1, num+1):
    if num % i == 0:
        cnt += 1

print(num)
print(cnt)

