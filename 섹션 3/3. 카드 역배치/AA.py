arr = list(range(1,21))

for _ in range(10):
    n, m = map(int, input().split())
    if n == 1 :
        arr[n - 1: m: 1] = arr[m - 1:: -1]
    else:
        arr[n - 1: m: 1] = arr[m - 1: n - 2: -1]

for i in arr:
    print(i, end = " ")