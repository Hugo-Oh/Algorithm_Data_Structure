
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

#행합은 어렵지않은데..
#행의 합
largest = -99999
for i in range(n):
    sum1 = sum2 = sum3 = sum4 = 0
    for j in range(n):
        sum1 += arr[i][j]
        sum2 += arr[j][i]

    #대각선 칭긔들
    sum3 += arr[i][i]
    sum4 += arr[-i][-i]

    if max(sum1, sum2, sum3, sum4) >= largest:
        largest = max(sum1, sum2, sum3, sum4)

print(largest)