A = "AbaAeCe"
a = dict()

for s in A:
    if s not in a:
        a[s] = A.count(s)

print(a)