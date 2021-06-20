"""import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
A = list(map(int, input().split()))
length = [0] * (N)

def LIS(A, index):
    if index == N - 1:
        return 1

    for i in range(index + 1, len(A)):
        if A[index] < A[i]:
            length[index] = max(length[index], LIS(A, i) + 1)

    return length[index]

res = LIS(A, 0)
print(res)

"""
n = int(input())
data = list(map(int, input().split()))

# LIS 알고리즘 구현
length = [1] * n  # 최소한 자기 자신일 때는 길이 1

for i in range(1, n):  # i = 1~n-1
    for j in range(i):  # j = 0~i-1
        if data[i] > data[j]:  # 기준 위치 i보다 작은 값이면...
            length[i] = max(length[i], length[j] + 1)
            # 현재 값과 j 위치 값+1 중에서 큰 값으로 갱신

print(max(length))