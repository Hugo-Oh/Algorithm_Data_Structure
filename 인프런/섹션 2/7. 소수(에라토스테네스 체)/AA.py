N = int(input())



#홀수만 체크하면 됨 2 제외
#3부터 홀수로 나누다가 나누어지는 순간 소수 아님!
#홀수의 딱 절반정도까지만 나누면 됨(아니면 루트..)

arr = [0] * (N+1)

cnt = 0

for i in range(2, N+1):
    if arr[i] == 0:
        cnt += 1
    for j in range(i,N + 1,i):
        arr[j] = 1

print(cnt)
