"""
괄호 회전하기
https://programmers.co.kr/learn/courses/30/lessons/76502
삼각 달팽이
https://programmers.co.kr/learn/courses/30/lessons/68645
이진 변환 반복하기
https://programmers.co.kr/learn/courses/30/lessons/70129
"""

S = "[](){}"
import sys
from _collections import deque
q = deque()

def rotate_left():
    q.append(q.popleft())
    return q

def check_s(S):
    stacked = []
    
    return True

print(check_s(S))
#max_ n개? n/2 + 1개.
#회전을 가장 많이 할 수 있는 경우? 어쩃뜬 회전은 0회 ~ 5회까지 실시 (6회 실시하면 다시 자기자신)

#회전따로, check_s 따로.
#회전은 popleft. append.
#체크는 함수로 만들자 () [] {} stacked = [],

# 시작은 무조건 ( { [ 아니면 break
# 마지막에 stacked가 비어있으면 True, 아니면 else
# 즉, ({[는 그냥 넣어버리고, ] } )는 나오는 순간 stacked[-1]을 확인하게 되는데 여기서 true가 되어야함.
# 최종결과가.


#체크해서 True가 되면 cnt += 1
#최종엔 answer = cnt\ return answer형식으로 마무리.