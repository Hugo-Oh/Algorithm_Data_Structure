"""import sys
sys.stdin = open("input.txt", "rt")


#하나하나 가면서 회문 판단
"""
def palin(x):
    cnt = 0
    for i in range(7):
        for j in range(7):
            sum_r = ""
            sum_c = ""
            if i < 3 and j < 3:
                for k in range(5):
                    sum_r += arr[i][j + k]
                    sum_c += arr[i + k][j]

                if sum_r[::] == sum_r[::-1]:
                    cnt += 1

                if sum_c[::] == sum_c[::-1]:
                    cnt += 1
            elif i >= 3 and j < 3:
                for k in range(5):
                    sum_r += arr[i][j + k]

                if sum_r[::] == sum_r[::-1]:
                    cnt += 1

            elif i < 3 and j >= 3:
                for k in range(5):
                    sum_c += arr[i + k][j]
                if sum_c[::] == sum_c[::-1]:
                    cnt += 1

    return cnt

arr = [list(map(str,input().split())) for _ in range (7)]
print(palin(arr))



