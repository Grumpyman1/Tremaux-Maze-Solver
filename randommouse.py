import random
import secrets

def get_points(mazeArray):
    global wallsList
    wallsList= []
    end = []
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

def check_type(currentLocation):
    routes = 0
    print(currentLocation[0]+1,currentLocation[1])
    print(wallsList)
    if [currentLocation[0]+1,currentLocation[1]] not in wallsList:
        routes += 1
    if [currentLocation[0],currentLocation[1]+1] not in wallsList:
        routes += 1
    if [currentLocation[0]-1, currentLocation[1]] not in wallsList:
        routes += 1
    if [currentLocation[0],currentLocation[1]-1] not in wallsList:
        routes += 1

    if routes == 1:
        return "deadend"
    if routes == 2:
        return "passage"
    if routes > 2:
        return "junction"

def getpath(mazeArray):
    print(mazeArray)
    wallsList, start, end = get_points(mazeArray)
    print(start)
    print(end)
    currentLocation = start
    previousLocation = []
    endfound = False
    route = []
    route.append(start)
    while endfound == False:
        if check_type(currentLocation) == "passage":
            if [currentLocation[0], currentLocation[1]+1] not in wallsList and (currentLocation[0], currentLocation[1]+1) != previousLocation:
                newPosition = (currentLocation[0], currentLocation[1]+1)
            if [currentLocation[0]+1, currentLocation[1]] not in wallsList and (currentLocation[0]+1, currentLocation[1]) != previousLocation:
                newPosition = (currentLocation[0]+1, currentLocation[1])
            if [currentLocation[0], currentLocation[1]-1] not in wallsList and (currentLocation[0], currentLocation[1]-1) != previousLocation:
                newPosition = (currentLocation[0], currentLocation[1]-1)
            if [currentLocation[0]-1, currentLocation[1]] not in wallsList and (currentLocation[0]-1, currentLocation[1]) != previousLocation:
                newPosition = (currentLocation[0]-1, currentLocation[1])

        if (check_type(currentLocation) == "deadend") and (previousLocation != []):
            newPosition = previousLocation
        else:
            if (check_type(currentLocation) == "deadend"):
                if [currentLocation[0], currentLocation[1]+1] not in wallsList:
                    newPosition = (currentLocation[0], currentLocation[1]+1)
                if [currentLocation[0]+1, currentLocation[1]] not in wallsList:
                    newPosition = (currentLocation[0]+1, currentLocation[1])
                if [currentLocation[0], currentLocation[1]-1] not in wallsList:
                    newPosition = (currentLocation[0], currentLocation[1]-1)
                if [currentLocation[0]-1, currentLocation[1]] not in wallsList:
                    newPosition = (currentLocation[0]-1, currentLocation[1])

        if check_type(currentLocation) == "junction":
            while True:
                #path = random.randrange(3)
                #path = secrets.randbelow(3)
                rng = random.SystemRandom()
                path = rng.randrange(4) #decide random direction
                print(path)
                #check if direction valid
                if check_type(currentLocation) != "junction":
                    break
                if (path == 0) and ((currentLocation[0],currentLocation[1]+1) != previousLocation) and ([currentLocation[0],currentLocation[1]+1] not in wallsList):
                    newPosition = (currentLocation[0], currentLocation[1]+1)
                    break
                if (path == 1) and ((currentLocation[0]+1,currentLocation[1]) != previousLocation) and ([currentLocation[0]+1,currentLocation[1]] not in wallsList):
                    newPosition = (currentLocation[0]+1, currentLocation[1])
                    break
                if (path == 2) and ((currentLocation[0],currentLocation[1]-1) != previousLocation) and ([currentLocation[0],currentLocation[1]-1] not in wallsList):
                    newPosition = (currentLocation[0], currentLocation[1]-1)
                    break
                if (path == 3) and ((currentLocation[0]-1,currentLocation[1]) != previousLocation) and ([currentLocation[0]-1,currentLocation[1]] not in wallsList):
                    newPosition = (currentLocation[0]-1, currentLocation[1])
                    break

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

wallsList=[]