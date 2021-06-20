import sys
sys.stdin = open("in1.txt", 'rt')

n, k = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = []
for i in range(0, len(arr1) - 2):
    for j in range(i + 1, len(arr1) - 1):
        for q in range(j + 1, len(arr1) - 0):
            arr2.append(arr1[i] + arr1[j] + arr1[q])


print(list(set(sorted(arr2, reverse = True)))[-k])