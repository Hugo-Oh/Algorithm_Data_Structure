import sys
sys.stdin = open("input.txt", "rt")

code = str(input())
N = len(code)
res = []
cnt = 0
def DFS(L, st):
    global code, cnt
    if L > N: #기저조건 1
        return

    if L == N: #정답
        res.append(st)
        cnt += 1
        return
    else:
        if code[L] == '0':
            DFS(L + 1, )
        elif 1 <= int(code[L:L+2]) < 27 and L+1 < N: #인경우는, 0을 포함하거나, 0이 단독!
            DFS(L + 1, st + chr((int(code[L]))+64))
            DFS(L + 2, st + chr((int(code[L:L + 2])) + 64))

        else:
            DFS(L+1, st + chr((int(code[L])) + 64))
DFS(0, "")
for s in res:
    print(s)
print(cnt)
