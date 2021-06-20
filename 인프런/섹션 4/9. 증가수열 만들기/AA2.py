import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))

cnt = 1
con = []

def popp(arr):
    if arr[0] > arr[-1]:
        res = arr.pop()
    else:
        res = arr.pop(0)
    return res

s = popp(arr)
con.append(s) #초기값 설정
print(con)

while True:
    s = popp(arr)
    if s >= con[-1]:
        con.append(s)
        cnt +=1
    else:
        break

print(cnt)




