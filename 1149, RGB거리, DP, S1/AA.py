import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))

for i in range(1, len(p)):#마지막까지
    p[i][0] = p[i][0]+min(p[i-1][1],p[i-1][2])#현재R+이전G,B중 최소값
    p[i][1] = p[i][1]+min(p[i-1][0],p[i-1][2])#현재G+이전R,B중 최소값
    p[i][2] = p[i][2]+min(p[i-1][0],p[i-1][1])#현재B+이전R,G중 최소값
print(min(p[n-1][0],p[n-1][1],p[n-1][2]))

