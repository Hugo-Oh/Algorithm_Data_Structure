import sys
sys.stdin = open("input.txt", "rt")

order = [(x, y) for x, y in enumerate(list(input()))]
order2 = "".join(list(map(lambda x : x[1], order)))

N = int(input())

for i in range(N):
    arr = list(input())
    res = []

    while len(arr) > 1:
        a = arr.pop(0)
        if a in order2:
            if any(a[0] > x[0] for x in res):
                print("NO")
                break

            else:
                res.append(a)
    else:
        print("Yes")








