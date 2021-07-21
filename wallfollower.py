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


def getpath(mazeArray):
    print(mazeArray)
    wallsList, start, end = get_points(mazeArray)
    print(start)
    print(end)
    route = []
    route.append(start)
    currentLocation = start
    previousLocation = []
    endfound = False
    firststep = True
    routenotfound = False

    if mazeArray[currentLocation[0]+1][currentLocation[1]] == '1' and mazeArray[currentLocation[0]-1][currentLocation[1]] == '1' and mazeArray[currentLocation[0]][currentLocation[1]+1] == '1':
        previousLocation = currentLocation
        newposition = (currentLocation[0], currentLocation[1]-1)
        currentLocation = newposition
        route.append(currentLocation)

    while endfound == False:
        # check if came from UP
        if (currentLocation[0], currentLocation[1] - 1) == previousLocation or firststep:
            if [currentLocation[0] - 1, currentLocation[1]] not in wallsList:
                newPosition = (currentLocation[0] - 1, currentLocation[1])
            elif [currentLocation[0], currentLocation[1] + 1] not in wallsList:
                newPosition = (currentLocation[0], currentLocation[1] + 1)
            elif [currentLocation[0] + 1, currentLocation[1]] not in wallsList:
                newPosition = (currentLocation[0] + 1, currentLocation[1])
            else:
                routenotfound = True

        # check if came from LEFT
        elif (currentLocation[0] - 1, currentLocation[1]) == previousLocation or firststep:
            if [currentLocation[0], currentLocation[1] + 1] not in wallsList:
                newPosition = (currentLocation[0], currentLocation[1] + 1)
            elif [currentLocation[0] + 1, currentLocation[1]] not in wallsList:
                newPosition = (currentLocation[0] + 1, currentLocation[1])
            elif [currentLocation[0], currentLocation[1] - 1] not in wallsList:
                newPosition = (currentLocation[0], currentLocation[1] - 1)
            else:
                routenotfound = True

        # check if came from DOWN
        elif (currentLocation[0], currentLocation[1] + 1) == previousLocation or firststep:
            if [currentLocation[0] + 1, currentLocation[1]] not in wallsList:
                newPosition = (currentLocation[0] + 1, currentLocation[1])
            elif [currentLocation[0], currentLocation[1] - 1] not in wallsList:
                newPosition = (currentLocation[0], currentLocation[1] - 1)
            elif [currentLocation[0] - 1, currentLocation[1]] not in wallsList:
                newPosition = (currentLocation[0] - 1, currentLocation[1])
            else:
                routenotfound = True

        # check if came from RIGHT
        elif (currentLocation[0] + 1, currentLocation[1]) == previousLocation or firststep:
            if [currentLocation[0], currentLocation[1] - 1] not in wallsList:
                newPosition = (currentLocation[0], currentLocation[1] - 1)
            elif [currentLocation[0] - 1, currentLocation[1]] not in wallsList:
                newPosition = (currentLocation[0] - 1, currentLocation[1])
            elif [currentLocation[0], currentLocation[1] + 1] not in wallsList:
                newPosition = (currentLocation[0], currentLocation[1] + 1)
            else:
                routenotfound = True

        if routenotfound:
            newPosition = previousLocation
            routenotfound = False
        firststep = False
        previousLocation = currentLocation
        currentLocation = newPosition

        if currentLocation == end:
            endfound = True
        route.append(currentLocation)
        print(currentLocation)
        print(previousLocation)
        print(route)
        if len(route) > 1000:
            print("exeded 1000")
            endfound = True
        print(len(route))
    return route


wallsList = []
