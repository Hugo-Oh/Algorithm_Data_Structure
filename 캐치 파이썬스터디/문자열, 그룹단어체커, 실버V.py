import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
res = 0
for _ in range(N):
    S = input()
    cap = len(set(S)) # 단어에서 중복되지 않는 문자열의 수

    for i in range(len(S)-1):
        if S[i] != S[i+1]: # 다르면 cap -1 하기
            cap -= 1

    if cap == 1: # 최종 cap이 1이면
        res += 1

print(res)

