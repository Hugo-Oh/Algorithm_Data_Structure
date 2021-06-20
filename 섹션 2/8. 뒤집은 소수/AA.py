"""N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는
프로그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력
한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하
여 프로그래밍 한다."""


def reverse(x):
    temp = ""
    for i in x:
        temp = i + temp
    ret = int(temp)
    return ret

def isPrime(x):
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True
n = input() #str으로 받기
arr = list(map(str, input().split()))

for num in arr:
    a = reverse(num)
    if isPrime(a) and a != 1:
        print(a, end = " ")


