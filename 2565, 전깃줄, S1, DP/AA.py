import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
#증가 or 같거나, 감소 or 같거나 증가하는거 3개, 감소하는거 6. 3개만 없애면 겹치는거 사라지나?



wire = []
for _ in range(N):
    i, v = map(int, input().split())

    wire.append((i, v))
wire.sort(key = lambda x : x[0])
wire = [x[1] for x in wire]
print(wire)

dp1 = [1 for _ in range(N)]
dp2 = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if wire[i] > wire[j]:
            dp1[i] = max(dp1[j] + 1, dp1[i])

wire = list(reversed(wire))
for i in range(N):
    for j in range(i):
        if wire[i] < wire[j]:
            dp2[i] = max(dp2[j] + 1, dp2[i])

print(dp1)
print(dp2)

# print(wire[:15])
# #print(dp_1[:15])
# #print(dp_2[:15])