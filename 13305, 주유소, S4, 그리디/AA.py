import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
km = input().split()
costArr = input().split()

costMin=1000000000
sumCost=0

for i in range(len(km)):
    temp = int(costArr[i])
    if costMin> temp:
        costMin=temp
    sumCost += int(km[i])*costMin

print(sumCost)