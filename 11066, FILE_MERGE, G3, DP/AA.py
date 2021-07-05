from itertools import combinations
import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))
arr = [sum(arr[:i]) for i in range(n)]
print(arr)










#

#
