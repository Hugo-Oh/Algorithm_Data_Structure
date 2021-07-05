def solution(strs, t):
    strs.sort(key=lambda x: len(x), reverse=True)
    DFS(0, 0, t, strs)
    return res if res < 20000 else -1

def remove_str(t, st):  # 왼쪽부터 딱 한번만 찾아서 그걸 제거하는 친구!
    i = t.index(st)
    t = t[:i] + t[i + len(st):]
    return t


def DFS(L, str_i, t, strs):
    global res
    if str_i >= len(strs):  # 넘어가버리면 없다는 뜻
        return -1
    if L > 20000:  # 기저조건 1
        return
    if t == "":  # 가 비어있다면 = 정답 발견한거!, 정답조건
        if L < res:
            res = L
        return

    st = strs[str_i]

    if st in t:  # 만약 str이 t에 있다면
        new_t = remove_str(t, st)
        DFS(L + 1, str_i, new_t, strs)
        DFS(L, str_i + 1, t, strs)
    else:
        DFS(L, str_i + 1, t, strs)

res = 21470000
print(solution(["app","ap","p","l","e","ple","pp"], "apple"))