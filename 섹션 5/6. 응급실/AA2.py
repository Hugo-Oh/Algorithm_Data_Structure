import sys
sys.stdin = open("in1.txt", "rt")

N, M = map(int, input().split())
arr = [(x, y) for x, y in enumerate(list(map(int, input().split())))]

#60을 꺼냈어, 60 왼쪽(앞)에 []더 높은거 있어? YES : 맨 뒤로 보내 OR NO : 진료 받아(그대로)
#50을 꺼냈어, 50 왼쪽에는 [60] YES : 맨 뒤로 보내
#40을 꺼냈어,
cnt = 0

while len(arr) > 1:
    temp = arr.pop(0)
    if any(temp[1] < x[1] for x in arr):
        arr.append(temp)

    else:
        cnt += 1
        if temp[0] == M:
            break

print(cnt)