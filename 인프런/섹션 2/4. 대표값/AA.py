N = int(input())
arr = list(map(int, input().split()))
avg = round(sum(arr) / N)
min = 99999
for index, value in enumerate(arr):
    tmp = abs(value - avg)
    if tmp < min:
        min = tmp
        score = value
        res = index + 1
    elif tmp == min:
        if value > score:
            score = value
            res = index + 1

print(avg, res)


#10
#45 73 66 87 92 67 75 79 75 80