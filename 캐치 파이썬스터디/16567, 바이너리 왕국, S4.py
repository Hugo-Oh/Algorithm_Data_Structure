import sys
#sys.stdin = open("input.txt", "rt")

#N, M = map(int, input().split())
#arr = [int(input()) for _ in range(N)]

def clean(i):
    if i >= N: #i인덱스가 벗어나면 리턴
        return

    if arr_copy[i] == 0: #0이면 리턴
        return

    else: # 1이면 0으로 만들고, 연속된 1도 0으로 만들어주기
        arr_copy[i] = 0
        clean( i + 1 )
        return True

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(M): #M*N으로 시간초과
    order = input().split()
    if order[0] == "0": #만약 최소외침 하라고 하면,
        cnt = 0
        arr_copy = arr.copy()
        for i in range(N):
            if clean(i) :
                cnt += 1
        print(cnt)

    else:
        arr[int(order[1]) - 1] = 1






