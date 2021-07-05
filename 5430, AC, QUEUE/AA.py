import sys
from _collections import deque
sys.stdin = open("input.txt", "rt")


R = int(input())
for _ in range(R):
    order = input()
    N = int(input())
    arr  = input().strip("[]").split(",")
    arr = arr if arr[0] else []
    arr = deque(map(int, arr))

    def R(arr):
        return deque(reversed(arr))

    def D(arr):
        if arr:
            arr.popleft()
        else:
            return "error"
        return

    for o in order:
        if o == "R":
            arr = R(arr)
        else:
            if D(arr) == "error":
                print("error")
            else:
                D(arr)

    print(arr)






