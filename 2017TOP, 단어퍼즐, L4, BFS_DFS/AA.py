strs = 	["ba", "an", "nan", "ban", "n"]
t = "banana"

strs.sort(key = lambda x : len(x), reverse = True)
print(strs)

def remove_str(t, str): # 왼쪽부터 딱 한번만 찾아서 그걸 제거하는 친구!
    i = t.index(str)
    t = t[:i] + t[i+ len(str):]
    return t

def DFS(L, str_i, t):
    global res
    if str_i >= len(strs): #넘어가버리면 없다는 뜻
        res = -1
        return
    if L > 20000: #기저조건 1
        return
    if t == "": #t가 비어있다면 = 정답 발견한거!, 정답조건 2
        if L < res:
            res = L
        return

    str = strs[str_i]

    if str in t: #만약 str이 t에 있다면
        new_t = remove_str(t, str)
        DFS(L+1, str_i, new_t)
        DFS(L, str_i+1, t)

    else:
        DFS(L, str_i + 1, t)
res = 21470000
DFS(0, 0, t)
print(res if res < 20000 else -1)

    #기저조건 정의하자


