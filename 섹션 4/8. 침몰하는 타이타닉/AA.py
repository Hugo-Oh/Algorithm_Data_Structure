import sys
from _collections import deque

sys.stdin = open("input.txt", "rt")

N, CAP = map(int, input().split())

deq = deque(sorted(list(map(int, input().split())),reverse = True))
print(deq)

def counter(cap):
    



"""
def count(cap):
    cnt = 1
    counter = 0

    for i in range(N):
        cap = cap - arr[i]
        if arr[i] <= cap and cnt <= 2:
            cap = cap - arr[i]
            cnt += 1
        else:
            counter += 1


    return counter

print(count(150))




"""