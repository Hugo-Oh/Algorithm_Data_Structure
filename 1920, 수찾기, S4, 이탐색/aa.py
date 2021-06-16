import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
res_list = list(map(int, input().split()))
res_list.sort()
M = int(input())
chk_list = list(map(int, input().split()))

for n in chk_list:
    l = 0
    r = N - 1
    checker = False
    while l <= r:
        mid = (l + r) // 2
        if res_list[mid] > n:
            r = mid - 1
        elif res_list[mid] < n:
            l = mid + 1
        else:
            checker = True
            break

    if checker:
        print(1)
    else:
        print(0)




