import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
A = list(map(int, input().split()))

print(A)

print(sum(A))

#가장 최악 = 다섯개가 다 똑같음 = 그말뜻은 전부 그 갭이 140에서 0임... 그럴수가 있지.
#가장 최고 =

l = min(A)
r = max(A)

def counter(L):
    loc = A[0]
    cnt = 1

    for i in A[1:]:
        if i > loc :
            loc = i
            cnt += 1
    return cnt

print(counter(1))

