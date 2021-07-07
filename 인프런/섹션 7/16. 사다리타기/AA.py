import sys
sys.stdin = open("input.txt", "rt")

board = [list(map(int, input().split())) for _ in range(10)]
ch = [[0 for _ in range(10)] for _ in range(10)]
#좌 우 먼저 보고 # y는 그대로,
#그게 없으면 밑으로 간다
#nx = [1, -1, 0]
#ny = [0, 0, 1]
checker = False
def DFS(now_y, now_x): #시작점은 각각.. 열번호는 now_x가 되겠져?
    global checker
    ch[now_y][now_x] = 1 #방문처리하기
    print(now_y, now_x)
    if now_y == 9 and board[now_y][now_x] != 2:
        checker = True
        return

    if board[now_y][now_x] == 2: #마지막까지 갔는데 2인경우, 근데 2인경우는 오직 now_y==9인 경우에만 존재함
        checker = True
        return
    
    else: #중간에 진행할 경우 # 딱 한번만 돌아갈텐데 왜 7 1이 두번나오지?
        if now_x + 1 < 10 and board[now_y][now_x + 1] == 1 and ch[now_y][now_x + 1] == 0: #방문한 적 없고, 오른쪽이 뚫려있다면
            DFS(now_y, now_x + 1)
            ch[now_y][now_x] = 0  # 방문처리하기

        elif now_x - 1 >= 0 and board[now_y][now_x -1] == 1 and ch[now_y][now_x - 1] == 0: #방문한 적 없고, 왼쪽이 뚫려있다면
            DFS(now_y, now_x - 1)
            ch[now_y][now_x] = 0  # 방문처리하기
            
        else: #그 외엔 무조건 밑으로(이 경우, 밑이 방문했다는 경우는 없고, 무조건 뚫려있으므로 방문여부 확인할 필요 없다.
            DFS(now_y + 1, now_x)
            ch[now_y][now_x] = 0  # 방문처리하기
            
DFS(0, 6)
print(checker)


        
            #
            # if 0 <= next_y < 10 and 0 <= next_x < 10:
            #
            #     print(next_y, next_x)
            #     if board[next_y][next_x] == 1 and next_x == now_x + 1: #오른먼저
            #         board[next_y][next_x] = 0
            #         DFS(next_y, next_x)
            #
            #     elif board[next_y][next_x] == 1 and next_x == now_x - 1: #왼쪽
            #         board[next_y][next_x] = 0
            #         DFS(next_y, next_x)
            #
            #     else:
            #         board[now_y][next_x] = 0
            #         DFS(now_y + 1, now_x)






