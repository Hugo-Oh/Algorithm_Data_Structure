import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
arr = []

for _ in range(N):
    arr.append(input())

temp_arr = []
for _ in range(N): # 최대길이 O(N^2)
    for i in range(N-1): #i랑 i+1번째 인덱스 비교하기
        if len(arr[i]) > len(arr[i+1]): # 길이가 짧은게 더 앞으로 오게하기
            arr[i], arr[i+1] = arr[i+1], arr[i]

        elif len(arr[i]) == len(arr[i+1]): # 길이가 같은경우
            tot_1 = 0
            tot_2 = 0
            for s in arr[i]:
                if s.isdecimal(): # 숫자면 해당 숫자를 합하기
                    tot_1 += int(s)

            for s in arr[i+1]: # 숫자면 해당 숫자를 합하기
                if s.isdecimal():
                    tot_2 += int(s)

            if tot_1 > tot_2: # 숫자의 합이 낮으면 자리교체
                arr[i], arr[i+1] = arr[i+1], arr[i]

            elif tot_1 == tot_2: # 합까지 같은경우 사전순으로 정렬하기
                for s1, s2 in zip(arr[i], arr[i + 1]):
                    if ord(s1) < ord(s2):  # 앞의 ord가 더 작다면 바로 종료
                        break

                    elif ord(s1) > ord(s2): # 앞의 ord가 같다가 어느순간 더 크다면
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                        break

for i in arr:
    print(i)


# 그렇게 n번 돌리면 될 것 같은데?

"""
1)A, B 의 길이가 다르면 , 짧은것이 먼저온다 LEN(A), LEN(B) 비교 가능.
2)길이가 같으면, A의 자리수의 합과 작은합을 가지는 것이 먼저온다. ISDECIMAL +=
3)그게 아니라면, 즉 합까지 같으면 사전순으로(숫자가 무조건 더 먼저온다)

말고리즘
1) 일단 길이순으로 쪽 정렬 어떻게? 길이를 반환하는 함수? 아니면?
len(x)를 키로 하는 것으로 정렬하면 되지 않을까. 해볼까.



"""

"""
from functools import cmp_to_key
n = int(input())
S = [input() for _ in range(n)]

def comp(a, b):
    if len(a) == len(b):
        sumA = sum([int(x) for x in a if x.isdecimal()])
        sumB = sum([int(x) for x in b if x.isdecimal()])
        if sumA == sumB:
            return -1 if a < b else 1
        else:
            return sumA - sumB
        
    else:
        return len(a) - len(b)

S.sort(key=cmp_to_key(comp))

print('\n'.join(S))
"""

"""
n = int(input())
S = [input() for _ in range(n)]
S = [(len(x), sum([int(y) for y in x if y.isdecimal()]), x) for x in S]
S.sort()

for x in S:
    print(x[2])
"""