"""a = 2

arr = [1, 2, 3]
cnt = 0
for i in arr:
    if a > i:
        cnt +=1

arr.insert(cnt, a)

print(arr)

"""
n = int(input())
arr_1 = list(map(int, input().split()))
m = int(input())
arr_2 = list(map(int, input().split()))

for num in arr_1:
    cnt = 0
    for i in arr_2:
        if num > i:
            cnt += 1
    
    arr_2.insert(cnt, num)

for i in arr_2:
    print(i, end = " ")