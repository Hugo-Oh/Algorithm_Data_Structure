columns = 5
rows = 5

A = [list(range((row-1) * columns+1, 1+(row-1) * columns + columns)) for row in range(1, rows+1)]
for i in A:
    print(i)
print()
A = [[A[i][j] for i in range(5)] for j in range(4, -1, -1)]
for i in A:
    print(i)
#a(n-1) + 1
