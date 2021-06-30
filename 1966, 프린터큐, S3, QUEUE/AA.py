from _collections import deque
import sys
sys.stdin = open("input.txt", "rt")
#input = sys.stdin.readline

R = int(input())
for _ in range(R):
    N, M = map(int, input().split())
    queue = deque(list(enumerate(list(map(int,input().split())))))

    cnt = 0
    while queue:
        i, v = queue.popleft()
        if not queue:
            print(cnt + 1)

        elif v >= max([x[1] for x in queue]):
            cnt += 1
            if i == M:
                print(cnt)
                break
        else:
            queue.append((i, v))





