from collections import deque
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
N = 5
K = 3
# 양방향

que = deque()
dis = [21470000 for _ in range(N)]
graph = [[0 for _ in range(N)] for _ in range(N)]
que.append(0) #1번부터 시작
dis[0] = 0
for y, x, cost in road:
    if graph[y-1][x-1] == 0:
        graph[y-1][x-1] = cost
        graph[x-1][y-1] = cost

    else:
        graph[y-1][x-1] = min(graph[y-1][x-1], cost)
        graph[x-1][y-1] = min(graph[x-1][y-1], cost)

for _ in graph:
    print(_)
x

def BFS():
    while que:
        now = que.popleft()
        for next in range(N): #해당노드
            if graph[now][next] != 0: #갈 길이 있다면
                if dis[next] > dis[now] + graph[now][next]:
                    dis[next] = dis[now] + graph[now][next]
                    que.append(next)

BFS()
print(len([x for x in dis if x <= K]))

# def BFS():
#     while que:
