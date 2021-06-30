a = [[1]]

x =[[1,0,0],[0,0,0],[0,0,0]]
for i in x:
    print(i)
print()
for i in range(n):
    for j in range(3):
        if i != 1 or j != 1:
            x[i][j] = x[3//3 - 1][3//3 - 1]
        else:
            x[i][j] = 0
for i in x:
    print(i)




