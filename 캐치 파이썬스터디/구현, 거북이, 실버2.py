import sys
sys.stdin = open("input.txt", "rt")

def turn_right():
    global cur_dir
    if cur_dir == (1, 0): # NORTH
        cur_dir = (0, 1)
    elif cur_dir == (0, 1): #WEST
        cur_dir = (-1, 0)
    elif cur_dir == (-1, 0): #SOUTH
        cur_dir = (0, -1)
    else: # EAST
        cur_dir = (1, 0) #NORTH

def turn_left():
    global cur_dir
    if cur_dir == (1, 0): # NORTH
        cur_dir = (0, -1)
    elif cur_dir == (0, -1): #WEST
        cur_dir = (-1, 0)
    elif cur_dir == (-1, 0): #SOUTH
        cur_dir = (0, 1)
    else: # EAST
        cur_dir = (1, 0) #NORTH

def move_foward():
    global y, x
    y = y + cur_dir[0]
    x = x + cur_dir[1]


def move_back():
    global x, y
    y = y - cur_dir[0]
    x = x - cur_dir[1]

def checker(y, x):
    global max_x, max_y, min_x, min_y
    if x > max_x:
        max_x = x
    elif x < min_x:
        min_x = x
    elif y < min_y:
        min_y = y
    elif y > max_y:
        max_y = y
    else:
        return





N = int(input())
for _ in range(N):
    max_y = 0
    max_x = 0
    min_y = 0
    min_x = 0

    cur_dir = (1, 0)
    y = 0
    x = 0
    order_list = input()
    for order in order_list:
        if order == "R":
            turn_right()

        elif order =="L":
            turn_left()

        elif order == "F":
            move_foward()
            checker(y, x)

        else :
            move_back()
            checker(y, x)


    res = abs((max_x - min_x) * (max_y - min_y))
    print(res)