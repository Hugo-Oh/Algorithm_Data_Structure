import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)] #이거 더 쉽게 할 수 없나. 있지요.

arr_plus = sorted([x for x in arr if x > 1])# 1보다 큰 양수부분
arr_minus = sorted([x for x in arr if x <= 0], reverse= True)#음수부분
arr_1 = [x for x in arr if x == 1]

tot = 0
stack = []

def max_sum(arr):
    global tot

    if not arr: #비어져있으면 아무것도 하지 말 것
        return

    for _ in range(len(arr)):
        temp = arr.pop()
        if stack: #하나 있으면
            tot += (temp * stack.pop()) # 곱해서 더하기
        else: #비어져있으면
            stack.append(temp)

    #다 한다음에 stack이 비어있으면? : 종료
    #else : stack.pop 더하기

    if stack: #stack에 하나 남아있으면
        tot += stack.pop() #비워버리기

tot += sum(arr_1)
max_sum(arr_plus)
max_sum(arr_minus)
print(tot)

"""ㅋㅋㅋㅋ 바본가 이 풀이법 실패. 정렬 먼저 해야할 것.
stack_plus = []
stack_minus = []
tot = 0


for _ in range(N):
    i = arr.pop()
    if i > 0
        if not stack_plus : #stack에 한개가 있으면
            tot += i * stack_plus.pop()
        else: #stack에 하나도 없으면 stack에 추가
            stack.append(i)

    else:
        if not stack_minus : #stack에 한개가 있으면
            tot += i * stack_minus.pop()
        else: #stack에 하나도 없으면 stack에 추가
            stack.append(i)

# 다 하고나서 stack이 하나씩 남아있으면 그대로 더하기
if stack_plus and stack_minus:
    tot += stack_plus.pop() + stack_minus.pop()

"""

