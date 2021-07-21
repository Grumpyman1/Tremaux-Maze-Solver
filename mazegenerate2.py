import random

# Init variables
wall = '1'
cell = '0'
unvisited = 'u'
height = 21
width = 21
#height = 21
#width = 21
maze = []


# setup
for i in range(0, height):
    line = []
    for j in range(0, width):
        if i%2 == 1 and j%2 == 1:
            line.append(unvisited)
        else:
            line.append(wall)
    maze.append(line)

row = []
for i in range(height):
    for y in range(height):
        row.append(maze[y][i])
    print(row)
    row = []

currentcell = (1, 1)
print(maze[1][1])
print(maze[currentcell[0]][currentcell[1]])
#print(maze[currentcell])


def check_if_unvisited_surround():
    surroundingunvisited = 0
    #up
    try:
        if maze[currentcell[0]-2][currentcell[1]] == "u":
            surroundingunvisited += 1
    except:
        pass

    #left
    try:
        if maze[currentcell[0]][currentcell[1]-2] == "u":
            surroundingunvisited += 1
    except:
        pass
    #down
    try:
        if maze[currentcell[0] + 2][currentcell[1]] == "u":
            surroundingunvisited += 1
    except:
        pass
    #right
    try:
        if maze[currentcell[0]][currentcell[1]+2] == "u":
            surroundingunvisited += 1
    except:
        pass

    if surroundingunvisited == 0:
        return False
    else:
        return True



cellslist = []
start = (currentcell[0], currentcell[1])
cellslist.append(currentcell)
#decide target cell
mazecomplete = False
while mazecomplete == False:

    # set current cell visited
    maze[currentcell[0]][currentcell[1]] = '0'
    validtarget = False
    while validtarget == False:
        try:
            currentcell = cellslist[-1]
        except:
            mazecomplete = True
            break
        check_if_unvisited_surround()
        rng = random.SystemRandom()
        direction = rng.randrange(4)
        #up
        if direction == 0:
            target = (currentcell[0]-2, currentcell[1])
        #left
        if direction == 1:
            target = (currentcell[0], currentcell[1]-2)
        #down
        if direction == 2:
            target = (currentcell[0]+2, currentcell[1])
        #right
        if direction == 3:
            target = (currentcell[0], currentcell[1]+2)

        if check_if_unvisited_surround():
            try:
                if maze[target[0]][target[1]] == "u":
                    #print("valid target")
                    validtarget = True
            except:
                pass
        else:
            cellslist.pop()
        #print(target)
        #print(currentcell)
    #remove wall between current and target
    if direction == 0:
        walltoremove = (currentcell[0]-1, currentcell[1])
    #left
    if direction == 1:
        walltoremove = (currentcell[0], currentcell[1]-1)
    #down
    if direction == 2:
        walltoremove = (currentcell[0]+1, currentcell[1])
    #right
    if direction == 3:
        walltoremove = (currentcell[0], currentcell[1]+1)

    maze[walltoremove[0]][walltoremove[1]] = '0'

    currentcell = target

    if check_if_unvisited_surround():
        cellslist.append(currentcell)
    else:
        try:
            cellslist.pop()
        except:
            pass
    print(cellslist)

    #print maze
    for i in range(height):
        for y in range(height):
            row.append(maze[y][i])
        print(row)
        row = []

    print()

#cuts for loops
cuts = 0
maxcuts = round((height*width)/40)
while cuts < maxcuts:
    randomx = random.randrange(width - 2) + 1
    randomy = random.randrange(height - 2) + 1

    #print(maze[randomx][randomy])
    if maze[randomx][randomy] == "1":
        if (maze[randomx][randomy+1] == "0" and maze[randomx][randomy-1] == "0")\
                and not (maze[randomx+1][randomy] == "0" or maze[randomx-1][randomy] == "0"):
            cuts += 1
            print(randomx, randomy)
            maze[randomx][randomy] = '0'
        if (maze[randomx+1][randomy] == "0" and maze[randomx-1][randomy] == "0")\
                and not (maze[randomx][randomy+1] == "0" or maze[randomx][randomy-1] == "0"):
            cuts += 1
            print(randomx, randomy)
            maze[randomx][randomy] = '0'

#correct start
maze[1][0] = '1'
maze[0][1] = '1'

#random start and end in deadend
#find dead end

def check_if_deadend(x, y):
    wallsaround = 0
    if maze[x+1][y] == '1':
        wallsaround += 1
    if maze[x][y+1] == '1':
        wallsaround += 1
    if maze[x-1][y] == '1':
        wallsaround += 1
    if maze[x][y-1] == '1':
        wallsaround += 1

    if wallsaround == 3:
        return True
    else:
        return False

while True:
    randx = random.randrange(width)
    randy = random.randrange(height)
    if maze[randx][randy] == '0':
        if check_if_deadend(randx, randy):
            maze[randx][randy] = '2'
            break

while True:
    randx = random.randrange(width)
    randy = random.randrange(height)
    if maze[randx][randy] == '0':
        if check_if_deadend(randx, randy):
            maze[randx][randy] = '3'
            break

#mark start and end
#maze[1][1] = '2'
#maze[width-2][height-2] = '3'