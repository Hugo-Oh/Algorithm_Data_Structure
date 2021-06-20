"""import sys
sys.stdin = open("input.txt", "rt")


#n = int(input())
#arr = list(map(int, input().split()))

arr = list(range(1, 7))

#전위순회
def DFS_pre(n):
    if n > 7:
        return
    print(n, end = " ")
    DFS_pre(2 * n)
    DFS_pre(2 *  n + 1)

#중위순회
def DFS_mid(n):
    if n > 7:
        return
    DFS_mid(2 * n)
    print(n, end = " ")
    DFS_mid(2 *  n + 1)

def DFS_post(n):
    if n > 7:
        return
    DFS_post(2 * n)
    DFS_post(2 *  n + 1)
    print(n, end = " ")

DFS_pre(1)
print("전위")

DFS_mid(1)
print("중위")
DFS_post(1)
print("후위")
"""