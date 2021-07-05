from _collections import deque
"""문제 설명
문자열에서 문자를 k개를 선택해 순서를 유지하며 이어 붙여 사전 순으로 가장 뒤에 오는 문자열을 만들려 합니다.

문자열 letters와 숫자 k가 매개변수로 주어집니다. letters에서 문자를 k개 선택해 순서를 유지하며 이어 붙여 만들 수 있는 문자열 중 사전 순으로 가장 뒤에 오는 것을 return 하도록 solution 함수를 완성해주세요.

제한사항
letters의 길이는 1 이상 500,000 이하입니다.
letters는 알파벳 소문자로만 이루어져 있습니다.
k는 1 이상 letters의 길이 이하인 자연수입니다.

출력 예
letters	k	return
"zbgaj"	3	"zgj"
입출력 예 설명
입출력 예 #1

사전 순으로 가장 뒤에 오는 문자열은 첫 번째, 세 번째, 다섯 번째 문자열을 선택해 이어 붙인 "zgj"입니다."""
letters = "zbgajc"
k = 3
q = deque()


for i in q:
    s = q.popleft()
    if
    stack.append(s)


#분할해야할듯

#쪼개고 다시 합쳐야하는 방식으로?

#쪼개서 보니까 stack에 쌓인거

#아니지, 그냥 무지성으로 순회하다가 ord(s)를 마지막으로 저장하자
def rank(arr, k): # 상위 k의 값을 가져오는 함수 Onlogn
    return sorted(arr, reverse = True,)[k - 1]
S = "zbagajjjl"
stack = []
l = [ord(s) for s in S]

for s in l:
    if stack and len(stack) < k and stack[-1] < s:
        print("hello")
        stack.pop()
        stack.append(s)
    else:
        stack.append(s)

check = rank(l, k)
l = [s for s in l if s >= check]
for s in l:
    if stack and len(stack) < k and stack[-1] < s:
        print("hello")
        stack.pop()
        stack.append(s)
    else:
        stack.append(s)

# 10개면 최솟값을 계속 빼야지ㅏ


print("stack", stack)
print("l", l)







l = [ord(s) for s in S]

def rank(arr, k): # 상위 k의 값을 가져오는 함수 Onlogn
    return sorted(arr, reverse = True,)[k - 1]

check = rank(l, k)
#여섯개를 뽑으라고 했어.

#l = [chr(s) for s in l if s >= check]
l = [s for s in l if s >= check]

#print("".join(l))


#print(l)


"""
["z"] => 마지막 g
"zb" =>마지막 b
"zbg" => 마지막 g
z b g a는 애초에 탈락
z b g j
"""
