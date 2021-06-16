import sys
sys.stdin = open("input.txt", "rt")


#a, b, c = map(int, input().split())
def w(a, b, c):
    if any((a == 0, b == 0, c == 0 )):
        return 1

    if any((a > 20, b > 20, c > 20)):
        return w(20, 20, 20)

    if (a < b < c):
        return w(a, b, c-1) + w(a, b-1, c-1) + w(a, b-1, c)

    else:

        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

Alist = [1]
Blist = [1]
Clist = [1]
print(w(1,1,1))
