def get_points(mazeArray):
    global wallsList
    wallsList = []
    for i in range(len(mazeArray)):
        for j in range(len(mazeArray[i])):
            current = []
            current.append(j)
            current.append(i)
            if mazeArray[j][i] == "1":
                wallsList.append(current)
            if mazeArray[j][i] == "2":
                start = j, i
            if mazeArray[j][i] == "3":
                end = j, i
    return wallsList, start, end


def step(loop, maze):
    for i in range(len(solvematrix)):
        for j in range(len(solvematrix[i])):
            if solvematrix[i][j] == loop:
                if i < len(solvematrix) - 1 and solvematrix[i + 1][j] == 0 and (maze[i + 1][j] == '0' or maze[i + 1][j] == '3'):
                    solvematrix[i + 1][j] = loop + 1
                    visitedcells.append((i+1, j))
                if j < len(solvematrix[i]) - 1 and solvematrix[i][j + 1] == 0 and (maze[i][j + 1] == '0' or maze[i][j + 1] == '3'):
                    solvematrix[i][j + 1] = loop + 1
                    visitedcells.append((i, j+1))
                if i > 0 and solvematrix[i - 1][j] == 0 and (maze[i - 1][j] == '0' or maze[i - 1][j] == '3'):
                    solvematrix[i - 1][j] = loop + 1
                    visitedcells.append((i-1, j))
                if j > 0 and solvematrix[i][j - 1] == 0 and (maze[i][j - 1] == '0' or maze[i][j - 1] == '3'):
                    solvematrix[i][j - 1] = loop + 1
                    visitedcells.append((i, j-1))


def print_solve_matrix():
    row = []
    for i in range(21):
        for y in range(21):
            row.append(solvematrix[y][i])
        print(row)
        row = []


def getpath(maze):
    visitedcells.clear()
    print(maze)
    wallsList, start, end = get_points(maze)
    print(start)
    print(end)
    # maze[end[0]][end[1]] = '0'
    route = []
    route.append(start)
    currentLocation = start
    previousLocation = []
    endfound = False
    solvematrix.clear()
    for i in range(len(maze)):
        solvematrix.append([])
        for j in range(len(maze[i])):
            solvematrix[-1].append(0)
    i, j = start
    solvematrix[start[0]][start[1]] = 1
    visitedcells.append((start[0], start[1]))
    loop = 0
    while solvematrix[end[0]][end[1]] == 0:
        loop += 1
        step(loop, maze)
        print_solve_matrix()

    print()
    print_solve_matrix()

    #gets route
    i, j = end[0], end[1]
    endvalue = solvematrix[i][j]
    route = [(i, j)]
    while endvalue > 1:
        if i > 0 and solvematrix[i - 1][j] == endvalue - 1:
            i = i - 1
            route.append((i, j))
            endvalue -= 1
        elif j > 0 and solvematrix[i][j - 1] == endvalue - 1:
            j = j - 1
            route.append((i, j))
            endvalue -= 1
        elif i < len(solvematrix) - 1 and solvematrix[i + 1][j] == endvalue - 1:
            i = i + 1
            route.append((i, j))
            endvalue -= 1
        elif j < len(solvematrix[i]) - 1 and solvematrix[i][j + 1] == endvalue - 1:
            j = j + 1
            route.append((i, j))
            endvalue -= 1

    print(visitedcells)
    print(route)

    return route, visitedcells


wallsList = []
solvematrix = []
visitedcells = []
