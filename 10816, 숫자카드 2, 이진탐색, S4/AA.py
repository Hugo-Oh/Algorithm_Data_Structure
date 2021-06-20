import sys
sys.stdin = open("input.txt", "rt")
N = int(input())
res_list = list(map(int,input().split()))
M = int(input())
chk_list = list(map(int,input().split()))
res_list.sort()
res = []
counter = 0
for n in chk_list:
    l = 0
    r = N
    counter_1 = 1
    counter_2 = 1

    while res_list[l] != M or res_list[r] != M:
        mid = (l + r) // 2

        if res_list[mid] < n:
            l = mid + 1

        elif res_list[mid] > n:
            r = mid - 1

        elif res_list[mid] == n:
            while all([mid-counter_1 >= 0, mid+counter_2 < N]) and (res_list[mid-counter_1] == n or res_list[mid+counter_2] == n):
                counter_1 -= 1
                counter_2 += 1
            cnt = counter_2 - counter_1 + 1
            res.append(cnt)

    counter += 1
    if counter == M-1:
        break

print(res)






