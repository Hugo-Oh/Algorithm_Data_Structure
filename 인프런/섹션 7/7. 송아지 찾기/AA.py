import sys
from collections import deque
#sys.stdin = open("in5.txt", "rt")

S, E = map(int, input().split())
PATH = [0 for _ in range(10001)] # 0은 방문하지 않음을 뜻함

q = deque()
#PATH[S] = 0
way = 5, 1, -1
def BFS(S):
    q.append(S)
    while q:
        now = q.popleft()
        if now == E:
            print(PATH[now])
            break
        for next in (now-1, now+1, now+5):
            if 1 <= next <= 10000 and not PATH[next]: #방문한적없으면
                PATH[next] = PATH[now] + 1
                q.append(next)
BFS(S)
#print(PATH)





