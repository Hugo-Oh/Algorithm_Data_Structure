"""import sys
sys.stdin = open("input.txt", "rt")
""""""“다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자
만 뽑기로 했습니다.”"""
N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

arr.sort(key = lambda x : (x[0], x[1]), reverse = True)

cnt = 0
largest = 0
for x, y in arr:
    if y > largest:
        largest = y
        cnt +=1

print(cnt)









