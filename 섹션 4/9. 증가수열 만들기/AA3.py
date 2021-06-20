import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))

lt = 0
rt = N-1
last = 0
res = ""
while lt <= rt:
    tmp = []
    if arr[lt] > last:
        tmp.append((arr[lt],"L"))

    if arr[rt] > last:
        tmp.append((arr[rt], "R"))

    tmp.sort(key = lambda x : x[0])

    if tmp:
        if tmp[0][1] == "L":
            last = tmp[0][0]
            res += "L"
            lt += 1
        else:
            last = tmp[0][0]
            res += "R"
            rt -= 1

    else:
        print(len(res))
        print(res)
        break









