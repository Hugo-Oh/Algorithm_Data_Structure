N = int(input())

temp1 = 0
temp2 = 0
arr = map(str, input().split())

for num in arr:
    total = 0


    for i in num:
        total += int(i)


    if total > temp1:
        temp2 = num

print(temp2)
