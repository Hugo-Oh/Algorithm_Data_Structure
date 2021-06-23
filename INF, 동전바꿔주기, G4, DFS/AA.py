import sys
sys.stdin = open("input.txt", "rt")

T = int(input())
k = int(input())

arr = [list(map(int, input().split())) for _ in range(k)]
arr.sort(key = lambda x : x[0], reverse = True)
print(arr)
def DFS(L, tot): #길이를 리턴
    if tot == 0:
        return L

    else:
        for i in range(T):
            if arr[i][1] > 0:
                arr[i][1] -= 1
                DFS(L + 1, tot - arr[i][0])

DFS(0, 20)




