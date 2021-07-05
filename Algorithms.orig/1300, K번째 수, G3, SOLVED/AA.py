import sys
sys.stdin = open("input.txt", "rt")


N = int(input())
k = int(input())

A = [[0] * N for _ in range(N)]
for i in range(0, N):
    for j in range(0, N):
        A[i][j] = (i+1) * (j+1) #이런느낌인건데 #이걸 하기때문에 연산이 너무 느려진다는ㄱ ㅓ지.

for i in A:
    print(i)
#그럼 이게 N*N중 몇번째에 포함되는지 알아야하고
#동시에 결국 시작값 기준으로 하면 되지 않나?

l = 0 #이게 인덱스 역할을, 뭘 기준으로 k를 알아낼지? N 묶음.... 첫번째값 기준? k라고 하면, 결국 그게 log2K?
r = N #이것도 인덱스 역할을, 3일때 7은 나머지 잖아. 그게 아니라 만약 10 0, 1, 2, 3 네덩이로 나뉘는데, 6번쨰라고 치면? 6/4를 한..1.x = 1번쨰 인덱스에 있다.
# 1000번째 찾으려고 하고, N=30이면? 안되지, 40이면? 1600이고, 1600/30 = 53.xx, 53번째에 있겠지, 그걸 발견했으면 다시 거기서 진행해내가는 구조로 하면?
# 그럼 결국 내가 필요한건, l=0, r,=N설정하고, mid가 언제 되어야한다? 미드가 K//N 이 되어야한다. (둘다 상수) 찾았으면? 다시 거기서부터 + K%N을 찾아가는 구조
target = k//N
res = 0
while l <= r:
    mid = (l + r) // 2
    if mid < target:
        l = mid + 1
    elif mid > target:
        r = mid - 1
    else:
        res = (l+2) * (mid+1)
        break

print(res)