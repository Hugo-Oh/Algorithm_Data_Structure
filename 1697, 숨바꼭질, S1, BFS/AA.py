#완전탐색
import sys
sys.stdin = open("input.txt", "rt")

#Greedy 조건 안됨 (부분 최적해가 전체 최적해가 된다는 보장 없음),
#완전탐색으로 가야할듯
#세가지, 결국 -1, +1, *2 셋중 하나의 선택지를 사용 할 수 있음
#-1, +1, *2 로 간것을 반복하다가 그 결과가 나왔을때 Min을 비교(최소거리로 간 것? yes 가장 적게 사용해서)
#dfs도 가능하긴한데, n과 k의 범위가 너무 깊어서 안될듯
import sys
from _collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [0] * 100001

def bfs(s, e):
    queue = deque()
    queue.append(s)
    while queue:
        now_s = queue.popleft()
        if now_s == e:
            return

        for next in [now_s - 1, now_s + 1, now_s * 2]:
            if 0 <= next < 100001 and graph[next] == 0:
                graph[next] = graph[now_s] + 1
                queue.append(next)
bfs(n, m)
print(graph[m])



