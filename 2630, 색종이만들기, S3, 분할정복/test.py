board = [[0,0,1,0,1], [0,0,0,0]]
print(all([all(x) for x in board]))

print(all([not any(x) for x in board]))

print([[x == 0 for x in y] for y in board])