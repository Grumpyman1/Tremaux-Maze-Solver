import tkinter
import turtle
import mazegenerate2
import importlib
import randommouse
import wallfollower as wall_follower
import bfsscript

#Generate a maze
def generate_maze():
    pathTurtle.clearstamps()
    player.showturtle()
    traveler.hideturtle()
    print("generate maze")
    enter_main()
    importlib.reload(mazegenerate2)
    generatedMaze = mazegenerate2.maze
    print(generatedMaze)
    row = []
    for i in range(mazegenerate2.width):
        for y in range(mazegenerate2.height):
            row.append(generatedMaze[y][i])
        print(row)
        row = []
    setup(generatedMaze)


def default_maze():
    pathTurtle.clearstamps()
    player.showturtle()
    traveler.hideturtle()
    enter_main()
    global defaultMaze
    print("default maze")
    setup(defaultMaze)


def undo_last_marker():
    print("last marker undo")
    try:
        if len(markOrderList) > 0:
            if markOrderList[len(markOrderList) - 1] == 'n':
                nMarkList.pop()
                print("removed last mark, was an n")
            if markOrderList[len(markOrderList) - 1] == 'x':
                xMarkList.pop()
                print("removed last mark, was an x")
            update_advice()
            print_marks()
            markOrderList.pop()
    except:
        return

#print function for comparisons
def print_route(path):
    if canvas.winfo_height() > canvas.winfo_width():
        offset = canvas.winfo_width()
    else:
        offset = canvas.winfo_height()
    wallSize = calculate_wall_size()
    traveler.turtlesize(wallSize / 40)
    print(path)
    print(path[0][0])
    print(path[0][1])
    traveler.goto(path[0][0] * wallSize - offset / 2 + wallSize / 2, path[0][1] * wallSize + offset / 2 - wallSize / 2)
    traveler.showturtle()
    pathTurtle.color("blue")
    for i in range(len(path)):
        screen_x = int(path[i][0]) * wallSize - offset / 2 + wallSize / 2
        screen_y = -int(path[i][1]) * wallSize + offset / 2 - wallSize / 2
        traveler.goto(screen_x, screen_y)
        pathTurtle.goto(screen_x, screen_y)
        # print("printed at ", screen_x, screen_y)
        pathTurtle.stamp()


def update_random_mouse_label(steps):
    stepsString = str(steps)
    if steps > 1000:
        label_score_randommouse.config(text=">1000")
    else:
        label_score_randommouse.config(text=stepsString)

def update_wallfollower_label(steps):
    stepsString = str(steps)
    if steps > 1000:
        label_score_wallfollower.config(text=">1000")
    else:
        label_score_wallfollower.config(text=stepsString)

def calculate_percentage_explored(path):
    #filter path
    filtered = []
    emptycells = 0
    for i in range(len(path)):
        if path[i] not in filtered:
            filtered.append(path[i])

    print(mazeArray)
    #count number of empty spaces in maze
    for i in range(len(mazeArray)):
        for j in range(len(mazeArray[i])):
            if mazeArray[i][j] != "1":
                emptycells += 1
            #print(mazeArray[i])

    #calculate percentage
    print(len(filtered))
    print(emptycells)
    percentage = round((len(filtered)/emptycells) * 100)
    return percentage

def random_mouse():
    print("random mouse")
    label_score_randommouse.config(text="Calculating...")
    pathTurtle.clearstamps()
    path = []
    path = randommouse.getpath(mazeArray)
    # calculate steps
    steps = len(path)
    # filter out repeats
    print_route(path)
    #path.clear()
    update_random_mouse_label(steps)
    percentage = calculate_percentage_explored(path)
    percentage_label = (percentage,"%")
    label_explored_randommouse.config(text=percentage_label)


def wallfollower():
    print("Wall Follower")
    label_score_wallfollower.config(text="Calculating...")
    pathTurtle.clearstamps()
    path = []
    print(mazeArray)
    path = wall_follower.getpath(mazeArray)
    steps = len(path)
    # filter out repeats
    print_route(path)
    #path.clear()
    update_wallfollower_label(steps)
    percentage = calculate_percentage_explored(path)
    percentage_label = (percentage, "%")
    label_explored_wallfollower.config(text=percentage_label)

def bfs_spread(allcells):
    if canvas.winfo_height() > canvas.winfo_width():
        offset = canvas.winfo_width()
    else:
        offset = canvas.winfo_height()
    wallSize = calculate_wall_size()
    traveler.turtlesize(wallSize / 40)

    pathTurtle.color("red")
    for i in range(len(allcells)):
        screen_x = int(allcells[i][0]) * wallSize - offset / 2 + wallSize / 2
        screen_y = -int(allcells[i][1]) * wallSize + offset / 2 - wallSize / 2
        traveler.goto(screen_x, screen_y)
        pathTurtle.goto(screen_x, screen_y)
        # print("printed at ", screen_x, screen_y)
        pathTurtle.stamp()

def bfs():
    print("BFS")
    label_score_bfs.config(text="Calculating...")
    pathTurtle.clearstamps()
    path, allcells = bfsscript.getpath(mazeArray)
    print(mazeArray)
    print(path)
    bfs_spread(allcells)
    print_route(path)
    percentage = calculate_percentage_explored(allcells)
    percentage_label = (percentage, "%")
    label_explored_bfs.config(text=percentage_label)
    steps = len(allcells)
    label_score_bfs.config(text=steps)

def print_path():
    pathTurtle.clearstamps()
    if canvas.winfo_height() > canvas.winfo_width():
        offset = canvas.winfo_width()
    else:
        offset = canvas.winfo_height()
    print(positionHistoryList)
    print(positionHistoryList[0][0])
    print(positionHistoryList[0][1])
    wallSize = calculate_wall_size()
    pathTurtle.color("blue")
    for i in range(len(positionHistoryList)):
        screen_x = int(positionHistoryList[i][0]) * wallSize - offset / 2 + wallSize / 2
        screen_y = -int(positionHistoryList[i][1]) * wallSize + offset / 2 - wallSize / 2
        pathTurtle.goto(screen_x, screen_y)
        # print("printed at ", screen_x, screen_y)
        pathTurtle.stamp()
    pathTurtle.color("red")

    redpostions = []
    for i in range(len(travelledCellsNotCurrentRoute)):
        if travelledCellsNotCurrentRoute[i] not in positionHistoryList:
            redpostions.append(travelledCellsNotCurrentRoute[i])
    print(redpostions)
    for i in range(len(redpostions)):
        screen_x = int(redpostions[i][0]) * wallSize - offset / 2 + wallSize / 2
        screen_y = -int(redpostions[i][1]) * wallSize + offset / 2 - wallSize / 2
        pathTurtle.goto((screen_x, screen_y))
        print("printed at ", screen_x, screen_y)
        pathTurtle.stamp()

def calculate_wall_size():
    if canvas.winfo_height() > canvas.winfo_width():
        smallestSide = canvas.winfo_width()
    else:
        smallestSide = canvas.winfo_height()
    # print(mazeArray)
    # print(len(mazeArray))
    # return smallestSide
    wallSize = round(smallestSide / len(mazeArray))
    # print(wallSize)
    return wallSize

# setup GUI
root = tkinter.Tk()
root.title("Tremaux maze solver")
root.geometry("1000x700")
menuWidth = 300
frame_turtle = tkinter.Frame(root, borderwidth="2", relief="ridge")
frame_menu = tkinter.Frame(root, borderwidth="2", relief="ridge", width=menuWidth)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame_turtle.grid(column=0, row=0, sticky="nw")
frame_menu.grid(column=1, row=0, sticky="nsew")
frame_menu.grid_propagate(0)

# creat all tkinter widgets

# label for maze
label_maze_options = tkinter.Label(frame_menu, text="Maze options", font=("courier", 20))
# button for default maze
button_maze_begin = tkinter.Button(frame_menu, text="Default Maze", command=default_maze)
# button for generated maze
#button_maze_generate = tkinter.Button(frame_menu, text="Generate Maze", command=genpopup())
button_maze_generate = tkinter.Button(frame_menu, text="Generate Maze", command=lambda : generate_maze())

# label for controlls
label_controls = tkinter.Label(frame_menu, text="Controls", font=("courier", 20))
# label left mouse
label_left_mouse = tkinter.Label(frame_menu, text="Left Mouse - Place Green Marker")
# label right mouse
label_right_mouse = tkinter.Label(frame_menu, text="Right Mouse - Place Red Marker")
# label arrow keys
label_arrow_keys = tkinter.Label(frame_menu, text="Arrow Keys - Navigate")

# label for current run
label_current_run = tkinter.Label(frame_menu, text="Current Run", font=("courier", 20))
# cells traveled total
label_cells_travelled = tkinter.Label(frame_menu, text="Cells Travelled = 0")
# current advice
label_current_advice = tkinter.Label(frame_menu, text="Advice", wraplength=menuWidth, justify="center",
                                     width=round(menuWidth / 7.7), height=5)
# undo_marker
button_undo_last_marker = tkinter.Button(frame_menu, text="Undo Marker", command=undo_last_marker)

#define labels
label_compare_method = tkinter.Label(frame_menu, text="Method")
label_compare_steps = tkinter.Label(frame_menu, text="Steps")
label_compare_explored = tkinter.Label(frame_menu, text="Explored")

#define random mouse labels
button_compare_randomouse = tkinter.Button(frame_menu, text="Random Mouse", command=random_mouse)
label_score_randommouse = tkinter.Label(frame_menu, text="0")
label_explored_randommouse = tkinter.Label(frame_menu, text="0")

#define wall follower labels
button_compare_wallfollower = tkinter.Button(frame_menu, text="Wall Follower", command=wallfollower)
label_score_wallfollower = tkinter.Label(frame_menu, text="0")
label_explored_wallfollower = tkinter.Label(frame_menu, text="0")

#define bfs labels
button_compare_bfs = tkinter.Button(frame_menu, text="BFS", command=bfs)
label_score_bfs = tkinter.Label(frame_menu, text="0")
label_explored_bfs = tkinter.Label(frame_menu, text="0")

#define user labels
button_show_user_solution = tkinter.Button(frame_menu, text="User Solution", command=print_path)
label_score_user = tkinter.Label(frame_menu,text="0")
label_explored_user = tkinter.Label(frame_menu, text="0")


label_maze_options.grid(column=0, row=0, columnspan=2, padx=10, pady=10, sticky='nsew')
button_maze_begin.grid(column=0, row=1, padx=10, pady=10)
button_maze_generate.grid(column=1, row=1, padx=10, pady=10)


def clear_compare_for_menu():
    button_compare_randomouse.grid_remove()
    label_score_randommouse.grid_remove()
    button_compare_wallfollower.grid_remove()
    label_score_wallfollower.grid_remove()
    button_show_user_solution.grid_remove()
    label_score_user.grid_remove()
    label_explored_user.grid_remove()
    label_explored_wallfollower.grid_remove()
    label_explored_randommouse.grid_remove()

    button_compare_bfs.grid_remove()
    label_score_bfs.grid_remove()
    label_explored_bfs.grid_remove()

    label_compare_method.grid_remove()
    label_compare_steps.grid_remove()
    label_compare_explored.grid_remove()


def enter_main():
    global InPlay
    InPlay = True

    global frame_menu
    clear_compare_for_menu()
    label_controls.grid(column=0, row=2, columnspan=2, padx=10, pady=10)
    label_left_mouse.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
    label_right_mouse.grid(column=0, row=4, columnspan=2, padx=10, pady=10)
    label_arrow_keys.grid(column=0, row=5, columnspan=2, padx=10, pady=10)
    label_current_run.grid(column=0, row=6, columnspan=2, padx=10, pady=10)
    label_cells_travelled.grid(column=0, row=7, columnspan=2, padx=10, pady=10)
    label_current_advice.grid(column=0, row=8, columnspan=2, padx=10, pady=10, sticky='nsew')
    button_undo_last_marker.grid(column=0, row=9, columnspan=2, padx=10, pady=10)



enter_main()


def clear_menu_for_compare():
    label_controls.grid_remove()
    label_left_mouse.grid_remove()
    label_right_mouse.grid_remove()
    label_arrow_keys.grid_remove()
    label_current_run.grid_remove()
    label_cells_travelled.grid_remove()
    label_current_advice.grid_remove()
    button_undo_last_marker.grid_remove()


def clear_turtle():
    player.clearstamps()
    wall.clearstamps()
    markerTurtle.clearstamps()
    goalTurtle.clearstamps()
    player.hideturtle()
    wall.hideturtle()
    goalTurtle.hideturtle()
    markerTurtle.hideturtle()





def print_walls(wallSize):
    if canvas.winfo_height() > canvas.winfo_width():
        offset = canvas.winfo_width()
    else:
        offset = canvas.winfo_height()
    for i in range(len(mazeArray)):
        for j in range(len(mazeArray[i])):
            character = mazeArray[j][i]
            # print(character)
            screen_x = j * wallSize - offset / 2 + wallSize / 2
            screen_y = -i * wallSize + offset / 2 - wallSize / 2

            if character == "1":
                wall.color("black")
                wall.goto(screen_x, screen_y)
                wall.stamp()
            if character == "2":
                wall.color("green")
                wall.goto(screen_x, screen_y)
                wall.stamp()
            if character == "3":
                wall.color("yellow")
                wall.goto(screen_x, screen_y)
                wall.stamp()





def setup_full_maze():
    print(canvas.winfo_width(), canvas.winfo_height())
    wallSize = calculate_wall_size()
    wall.turtlesize(wallSize / 20)
    pathTurtle.turtlesize(wallSize / 40)
    print_walls(wallSize)
    print_path()


def enter_compare():
    global InPlay
    global totalCellsTravelled
    InPlay = False
    global frame_menu
    clear_turtle()
    clear_menu_for_compare()
    # frame_menu.grid_forget()

    #main interface for new maze
    label_maze_options.grid(column=0, row=0, columnspan=2, padx=10, pady=10, sticky='nsew')
    button_maze_begin.grid(column=0, row=1, padx=10, pady=10)
    button_maze_generate.grid(column=1, row=1, padx=10, pady=10)

    #labels
    label_compare_method.grid(column=0, row=2, padx=10, pady=10)
    label_compare_steps.grid(column=1, row=2, padx=10, pady=10)
    label_compare_explored.grid(column=2, row=2, padx=10, pady=10)

    #user solution
    button_show_user_solution.grid(column=0, row=3, padx=10, pady=10)
    label_score_user.grid(column=1, row=3, padx=10, pady=10)
    label_explored_user.grid(column=2, row=3, padx=10, pady=10)
    label_score_user.config(text=totalCellsTravelled)

    #random mouse
    button_compare_randomouse.grid(column=0, row=4, padx=10, pady=10)
    label_score_randommouse.grid(column=1, row=4, padx=10, pady=10)
    label_explored_randommouse.grid(column=2, row=4, padx=10, pady=10)

    #wall follower
    button_compare_wallfollower.grid(column=0, row=5, padx=10, pady=10)
    label_score_wallfollower.grid(column=1, row=5, padx=10, pady=10)
    label_explored_wallfollower.grid(column=2, row=5, padx=10, pady=10)

    #bfs
    button_compare_bfs.grid(column=0, row=6, padx=10, pady=10)
    label_score_bfs.grid(column=1, row=6, padx=10, pady=10)
    label_explored_bfs.grid(column=2, row=6, padx=10, pady=10)

    # frame_menu.grid()
    label_score_randommouse.config(text="Click to calculate")
    label_score_wallfollower.config(text="Click to calculate")
    label_score_bfs.config(text="click to calculate")
    label_explored_randommouse.config(text="0%")
    label_explored_wallfollower.config(text="0%")
    label_explored_bfs.config(text="0%")
    setup_full_maze()

    #user solution percentage#
    percentage = calculate_percentage_explored(travelledCellsNotCurrentRoute)
    percentage = percentage + calculate_percentage_explored(positionHistoryList)
    percentage_label = (percentage, "%")
    label_explored_user.config(text=percentage_label)


print(frame_menu.winfo_width())
print(frame_turtle.winfo_width())

# maze
level_1 = [
    "1111111111111111111111111",
    "1110000000001000000000001",
    "1211111111101011111111101",
    "1010000000001011110111101",
    "1011111111100000000000001",
    "1011111111111111111101101",
    "1000000000000100000101101",
    "1110111111110101110101101",
    "1110100001110101111100001",
    "1110111101110000000101101",
    "1110110000010111110101101",
    "1110110111010100000001101",
    "1110000000010101111111101",
    "1110111111110101111111101",
    "1110101000000100000000001",
    "1000101011111111111111111",
    "1010101011111111111111111",
    "1010000011111111111111111",
    "1010111011111111111111111",
    "1010111000000000001111111",
    "1010111111111111101111111",
    "1010111111111111101111111",
    "1011111111111111101111111",
    "1000000000000000100000031",
    "1111111111111111111111111",
]


# check keys
def up_pressed():
    if InPlay:
        print("up pressed")
        global pypos
        global pxpos
        newxpos = pxpos
        newypos = pypos - 1
        if (newxpos, newypos) not in wallsList:
            update_pos(newxpos, newypos)
            player.setheading(90)


def down_pressed():
    if InPlay:
        print("down")
        global pypos
        global pxpos
        newxpos = pxpos
        newypos = pypos + 1
        if (newxpos, newypos) not in wallsList:
            update_pos(newxpos, newypos)
            player.setheading(270)


def left_pressed():
    if InPlay:
        print("left")
        global pypos
        global pxpos
        newxpos = pxpos - 1
        newypos = pypos
        if (newxpos, newypos) not in wallsList:
            update_pos(newxpos, newypos)
            player.setheading(180)


def right_pressed():
    if InPlay:
        print("right")
        global pypos
        global pxpos
        newxpos = pxpos + 1
        newypos = pypos
        if (newxpos, newypos) not in wallsList:
            update_pos(newxpos, newypos)
            player.setheading(0)


def x_pressed():
    if InPlay:
        print("x pressed")
        print(frame_turtle.winfo_pointerx())
        print(frame_turtle.winfo_pointery())


def n_pressed():
    if InPlay:
        print("n pressed")


def drawsomething(label):
    value = label.char
    print("hello")
    print(value, "A button is pressed")


def check_on_canvas():
    x, y = root.winfo_pointerxy()
    widget = root.winfo_containing(x, y)
    widgetStr = str(widget)
    print(widgetStr)
    if widgetStr == ".!frame.!canvas":
        return True
    else:
        return False


def mouse_click_left(event):
    if InPlay:
        global pxpos
        global pypos
        print(event.x)
        print(event.y)
        if check_if_junction() != 'junction':
            print("not a junction")
            return
        if check_on_canvas() == False:
            return
        realx = (event.x - canvas.winfo_width() / 2)
        realy = -(event.y - canvas.winfo_height() / 2)
        direction = identify_direction(realx, realy)
        if direction == "invalid":
            print("invalid")
            return
        cell = identify_cell(direction)
        ppos = pxpos, pypos
        print(cell, ppos)
        cellandjunction = []
        cellandjunction.append(cell)
        cellandjunction.append(ppos)

        if cell in wallsList:
            print("invalid choice, that is a wall")
        elif (cellandjunction in xMarkList) or (cellandjunction in nMarkList):
            print('cell is already marked')
        else:
            print('you have clicked cell ', cell)
            nMarkList.append(cellandjunction)
            markOrderList.append("n")
            print(nMarkList)
            print_marks()
            update_advice()


def mouse_click_right(event):
    if InPlay:
        global pxpos
        global pypos
        print(event.x)
        print(event.y)
        if check_if_junction() != 'junction':
            print("not a junction")
            return
        if check_on_canvas() == False:
            return
        realx = (event.x - canvas.winfo_width() / 2)
        realy = -(event.y - canvas.winfo_height() / 2)
        direction = identify_direction(realx, realy)
        if direction == "invalid":
            print("invalid")
            return
        cell = identify_cell(direction)
        ppos = pxpos, pypos
        print(cell, ppos)
        cellandjunction = []
        cellandjunction.append(cell)
        cellandjunction.append(ppos)

        if cell in wallsList:
            print("invalid choice, that is a wall")
        elif (cellandjunction in xMarkList) or (cellandjunction in nMarkList):
            print('cell is already marked')
        else:
            print('you have clicked cell ', cell)
            xMarkList.append(cellandjunction)
            markOrderList.append("x")
            print(xMarkList)
            print_marks()
            update_advice()


def print_marks():
    markerTurtle.clearstamps()
    for i in range(len(surroundingCoords)):
        for j in range(len(surroundingCoords)):
            currentcoord = []
            currentcoord.append(surroundingCoords[i])
            currentcoord.append(surroundingCoords[j])
            if (currentcoord) in xMarkList:
                print(surroundingCoords[i], surroundingCoords[j])
                if (surroundingCoords[i][0] - 1 == surroundingCoords[j][0]) \
                        and surroundingCoords[i][1] == surroundingCoords[j][1]:
                    markPositionfromjunction = "right"
                if (surroundingCoords[i][0] + 1 == surroundingCoords[j][0]) \
                        and surroundingCoords[i][1] == surroundingCoords[j][1]:
                    markPositionfromjunction = "left"
                if (surroundingCoords[i][0] == surroundingCoords[j][0]) \
                        and surroundingCoords[i][1] + 1 == surroundingCoords[j][1]:
                    markPositionfromjunction = "up"
                if (surroundingCoords[i][0] == surroundingCoords[j][0]) \
                        and surroundingCoords[i][1] - 1 == surroundingCoords[j][1]:
                    markPositionfromjunction = "down"
                markcanvas(surroundingCoords[j], markPositionfromjunction, j, "x")
            if (currentcoord) in nMarkList:
                print(surroundingCoords[i], surroundingCoords[j])
                if (surroundingCoords[i][0] - 1 == surroundingCoords[j][0]) \
                        and surroundingCoords[i][1] == surroundingCoords[j][1]:
                    markPositionfromjunction = "right"
                if (surroundingCoords[i][0] + 1 == surroundingCoords[j][0]) \
                        and surroundingCoords[i][1] == surroundingCoords[j][1]:
                    markPositionfromjunction = "left"
                if (surroundingCoords[i][0] == surroundingCoords[j][0]) \
                        and surroundingCoords[i][1] + 1 == surroundingCoords[j][1]:
                    markPositionfromjunction = "up"
                if (surroundingCoords[i][0] == surroundingCoords[j][0]) \
                        and surroundingCoords[i][1] - 1 == surroundingCoords[j][1]:
                    markPositionfromjunction = "down"
                markcanvas(surroundingCoords[j], markPositionfromjunction, j, "n")


def markcanvas(xy, direction, cellnumber, mark):
    print(xy)
    print(direction)
    print(cellposition[cellnumber])
    if direction == "right":
        markerTurtle.goto(cellposition[cellnumber][0] + round(cellSize / 2 - cellSize / 8), cellposition[cellnumber][1])
        if mark == "x":
            markerTurtle.color("red")
            markerTurtle.stamp()
        if mark == "n":
            markerTurtle.color("green")
            markerTurtle.stamp()
    if direction == "left":
        markerTurtle.goto(cellposition[cellnumber][0] - round(cellSize / 2 - cellSize / 8), cellposition[cellnumber][1])
        if mark == "x":
            markerTurtle.color("red")
            markerTurtle.stamp()
        if mark == "n":
            markerTurtle.color("green")
            markerTurtle.stamp()
    if direction == "up":
        markerTurtle.goto(cellposition[cellnumber][0], cellposition[cellnumber][1] + round(cellSize / 2 - cellSize / 8))
        if mark == "x":
            markerTurtle.color("red")
            markerTurtle.stamp()
        if mark == "n":
            markerTurtle.color("green")
            markerTurtle.stamp()
    if direction == "down":
        markerTurtle.goto(cellposition[cellnumber][0], cellposition[cellnumber][1] - round(cellSize / 2 - cellSize / 8))
        if mark == "x":
            markerTurtle.color("red")
            markerTurtle.stamp()
        if mark == "n":
            markerTurtle.color("green")
            markerTurtle.stamp()


# define canvas
canvas = tkinter.Canvas(frame_turtle, width=700, height=700, bg="black")
#canvas.grid(column=0, row=0)

#canvas = turtle.ScrolledCanvas(root)
canvas.pack(side=tkinter.LEFT)
screen = turtle.TurtleScreen(canvas)
screen.tracer(0)

global player
global wall
global marker

# setup player turtle
player = turtle.RawTurtle(canvas)
player.showturtle()
player.color("blue")
player.shape("triangle")
player.speed(0)
player.penup()
player.goto(0, 0)

# setup wall turtle
wall = turtle.RawTurtle(screen)
wall.color("black")
wall.shape("square")
wall.speed(0)
wall.penup()
wall.goto(100, 100)

# setup mouse location turtle
locationTurtle = turtle.RawTurtle(canvas)
locationTurtle.shape("square")
locationTurtle.color("white")
locationTurtle.penup()
locationTurtle.speed(0)
locationTurtle.hideturtle()

# setup marker turtle
markerTurtle = turtle.RawTurtle(screen)
markerTurtle.shape("square")
markerTurtle.color("red")
markerTurtle.penup()
markerTurtle.speed(0)
markerTurtle.hideturtle()

# setup goal turtle
goalTurtle = turtle.RawTurtle(screen)
goalTurtle.shape("circle")
goalTurtle.color("yellow")
goalTurtle.penup()
goalTurtle.speed(0)
goalTurtle.hideturtle()

# setup path turtle
pathTurtle = turtle.RawTurtle(canvas)
pathTurtle.shape("circle")
pathTurtle.color("blue")
pathTurtle.penup()
pathTurtle.speed(0)
pathTurtle.hideturtle()

# setup route traveler
traveler = turtle.RawTurtle(canvas)
traveler.shape("circle")
traveler.color("green")
traveler.penup()
traveler.speed(0)
traveler.hideturtle()

print(canvas.winfo_width())
print(canvas.winfo_height())


def identify_cell(direction):
    if direction == 'up':
        clickedCoord = (pxpos, pypos - 1)
    if direction == 'down':
        clickedCoord = (pxpos, pypos + 1)
    if direction == 'left':
        clickedCoord = (pxpos - 1, pypos)
    if direction == 'right':
        clickedCoord = (pxpos + 1, pypos)
    return clickedCoord


def check_if_junction():
    options = 0
    if (pxpos + 1, pypos) not in wallsList:
        options += 1
    if (pxpos - 1, pypos) not in wallsList:
        options += 1
    if (pxpos, pypos + 1) not in wallsList:
        options += 1
    if (pxpos, pypos - 1) not in wallsList:
        options += 1
    if options > 2:
        cellType = "junction"
    if options == 2:
        cellType = "passage"
    if options == 1:
        cellType = "deadend"
    # print("at a ", cellType)
    return cellType


def setup_array(level):
    for y in range(len(level)):
        currentrow = []
        for x in range(len(level[y])):
            character = level[x][y]
            currentrow.append(character)

        print(currentrow)
        mazeArray.append(currentrow)
    print(mazeArray)


def place_player():
    for i in range(len(mazeArray)):
        for j in range(len(mazeArray[i])):
            character = mazeArray[i][j]
            if character == "2":
                global pxpos
                global pypos
                update_pos(i, j)
                # pxpos = i
                # pypos = j
                print(i)
                print(j)


def update_surounding_coords():
    global pxpos
    global pypos
    global surroundingCoords
    surroundingCoords[0] = pxpos - 1, pypos - 1
    surroundingCoords[1] = pxpos, pypos - 1
    surroundingCoords[2] = pxpos + 1, pypos - 1
    surroundingCoords[3] = pxpos - 1, pypos
    surroundingCoords[4] = pxpos, pypos
    surroundingCoords[5] = pxpos + 1, pypos
    surroundingCoords[6] = pxpos - 1, pypos + 1
    surroundingCoords[7] = pxpos, pypos + 1
    surroundingCoords[8] = pxpos + 1, pypos + 1


def draw_surroundings():
    wall.clearstamps()
    if mazeArray[pxpos - 1][pypos - 1] == "1":
        wall.goto(cellposition[0])
        wall.stamp()
    if mazeArray[pxpos][pypos - 1] == "1":
        wall.goto(cellposition[1])
        wall.stamp()
    if mazeArray[pxpos + 1][pypos - 1] == "1":
        wall.goto(cellposition[2])
        wall.stamp()
    if mazeArray[pxpos - 1][pypos] == "1":
        wall.goto(cellposition[3])
        wall.stamp()
    if mazeArray[pxpos + 1][pypos] == "1":
        wall.goto(cellposition[5])
        wall.stamp()
    if mazeArray[pxpos - 1][pypos + 1] == "1":
        wall.goto(cellposition[6])
        wall.stamp()
    if mazeArray[pxpos][pypos + 1] == "1":
        wall.goto(cellposition[7])
        wall.stamp()
    if mazeArray[pxpos + 1][pypos + 1] == "1":
        wall.goto(cellposition[8])
        wall.stamp()


def set_cell_positions():
    global cellSize
    if (canvas.winfo_height() / 4) * 3 > canvas.winfo_width():
        smallestlength = canvas.winfo_width()
    else:
        smallestlength = canvas.winfo_height()
    cellSize = smallestlength / 3
    print(cellSize)
    cellposition[0] = (-cellSize, cellSize)
    cellposition[1] = (0, cellSize)
    cellposition[2] = (cellSize, cellSize)
    cellposition[3] = (-cellSize, 0)
    cellposition[4] = (0, 0)
    cellposition[5] = (cellSize, 0)
    cellposition[6] = (-cellSize, -cellSize)
    cellposition[7] = (0, -cellSize)
    cellposition[8] = (cellSize, -cellSize)
    wall.turtlesize(cellSize / 20)
    player.turtlesize(cellSize / 60)
    markerTurtle.turtlesize(cellSize / 100)


def create_walls_list():
    for i in range(len(mazeArray)):
        for j in range(len(mazeArray[i])):
            character = mazeArray[i][j]
            if character == "1":
                wallsList.append((i, j))


def update_position_history():
    global totalCellsTravelled
    if backTrack == False:
        positionHistoryList.append((pxpos, pypos))
    else:
        travelledCellsNotCurrentRoute.append(positionHistoryList.pop())
    totalCellsTravelled += 1
    print(positionHistoryList)
    print(travelledCellsNotCurrentRoute)


def check_if_backtrack():
    global pxpos
    global pypos
    global backTrack
    if len(positionHistoryList) > 0:
        if (pxpos, pypos) == positionHistoryList[len(positionHistoryList) - 2]:
            backTrack = True
        else:
            backTrack = False
    else:
        backtrack = False


def update_cells_travelled_label():
    global totalCellsTravelled
    total = len(positionHistoryList) + len(travelledCellsNotCurrentRoute)
    labelText = "cells Travelled = " + str(totalCellsTravelled)
    label_cells_travelled.config(text=labelText)


def check_if_junction_marked_n():
    marked = False
    global pxpos
    global pypos
    playerpos = (pxpos, pypos)
    for i in range(len(nMarkList)):
        if nMarkList[i][0] == surroundingCoords[1] \
                and nMarkList[i][1] == playerpos:
            print("green marker up")
            marked = True
        if nMarkList[i][0] == surroundingCoords[3] \
                and nMarkList[i][1] == playerpos:
            print("green marker left")
            marked = True
        if nMarkList[i][0] == surroundingCoords[5] \
                and nMarkList[i][1] == playerpos:
            print("green marker right")
            marked = True
        if nMarkList[i][0] == surroundingCoords[7] \
                and nMarkList[i][1] == playerpos:
            print("green marker down")
            marked = True
    return marked


def check_if_junction_marked_x():
    marked = False
    global pxpos
    global pypos
    playerpos = (pxpos, pypos)
    for i in range(len(xMarkList)):
        if xMarkList[i][0] == surroundingCoords[1] \
                and xMarkList[i][1] == playerpos:
            print("red marker up")
            marked = True
        if xMarkList[i][0] == surroundingCoords[3] \
                and xMarkList[i][1] == playerpos:
            print("red marker left")
            marked = True
        if xMarkList[i][0] == surroundingCoords[5] \
                and xMarkList[i][1] == playerpos:
            print("red marker right")
            marked = True
        if xMarkList[i][0] == surroundingCoords[7] \
                and xMarkList[i][1] == playerpos:
            print("red marker down")
            marked = True
    return marked


def red_mark_position():
    for i in range(len(xMarkList)):
        if backTrack == False:
            if positionHistoryList[len(positionHistoryList) - 2] == xMarkList[i][0]:
                return "JustTraversed"
            else:
                return "NotJustTraversed"


def most_recent_green_mark_at_junction():
    global pxpos
    global pypos
    print(nMarkList[len(nMarkList) - 1][1])
    position = []
    position.append(pxpos)
    position.append(pypos)
    print(position)
    if nMarkList[len(nMarkList) - 1][1] == (pxpos, pypos):
        return True
    else:
        return False


def analyse_junction():
    global pxpos
    global pypos
    directionfrom = ""
    upinfo = ""
    leftinfo = ""
    rightinfo = ""
    downinfo = ""
    playerpos = (pxpos, pypos)
    for i in range(len(nMarkList)):
        if nMarkList[i][0] == surroundingCoords[1] \
                and nMarkList[i][1] == playerpos:
            upinfo = "n"
        if nMarkList[i][0] == surroundingCoords[3] \
                and nMarkList[i][1] == playerpos:
            print("green marker left")
            leftinfo = "n"
        if nMarkList[i][0] == surroundingCoords[5] \
                and nMarkList[i][1] == playerpos:
            print("green marker right")
            rightinfo = "n"
        if nMarkList[i][0] == surroundingCoords[7] \
                and nMarkList[i][1] == playerpos:
            print("green marker down")
            downinfo = "n"
    for i in range(len(xMarkList)):
        if xMarkList[i][0] == surroundingCoords[1] \
                and xMarkList[i][1] == playerpos:
            print("red marker up")
            upinfo = "x"
        if xMarkList[i][0] == surroundingCoords[3] \
                and xMarkList[i][1] == playerpos:
            print("red marker left")
            leftinfo = "x"
        if xMarkList[i][0] == surroundingCoords[5] \
                and xMarkList[i][1] == playerpos:
            print("red marker right")
            rightinfo = "x"
        if xMarkList[i][0] == surroundingCoords[7] \
                and xMarkList[i][1] == playerpos:
            print("red marker down")
            downinfo = "x"
    if surroundingCoords[1] in wallsList:
        upinfo = "w"
    if surroundingCoords[3] in wallsList:
        leftinfo = "w"
    if surroundingCoords[5] in wallsList:
        rightinfo = "w"
    if surroundingCoords[7] in wallsList:
        downinfo = "w"

    if upinfo == "":
        upinfo = "u"
    if downinfo == "":
        downinfo = "u"
    if leftinfo == "":
        leftinfo = "u"
    if rightinfo == "":
        rightinfo = "u"

    if backTrack:
        lastposition = travelledCellsNotCurrentRoute[len(travelledCellsNotCurrentRoute) - 1]
    else:
        lastposition = positionHistoryList[len(positionHistoryList) - 2]
    if lastposition == surroundingCoords[1]:
        directionfrom = 0
    if lastposition == surroundingCoords[3]:
        directionfrom = 1
    if lastposition == surroundingCoords[5]:
        directionfrom = 2
    if lastposition == surroundingCoords[7]:
        directionfrom = 3

    info = []
    info.append(upinfo)
    info.append(leftinfo)
    info.append(rightinfo)
    info.append(downinfo)
    info.append(directionfrom)
    return info


def update_advice():
    global backTrack
    mostrecentpos = positionHistoryList[len(positionHistoryList) - 1]
    print("new advice is")
    if check_if_junction() == "deadend" and len(positionHistoryList) == 1:
        print("Traverse forward through the maze until you reach a junction")
        adviceText = "Traverse forward through the maze until you reach a junction"
    if check_if_junction() == "deadend" and len(positionHistoryList) > 1:
        print("Deadend reached, backtrack to the previous junction")
        adviceText = "Deadend reached, backtrack to the previous junction"
    if check_if_junction() == "passage" and backTrack == False:
        print("Keep heading forward until you reach a junction")
        adviceText = "Keep heading forward until you reach a junction"
    if check_if_junction() == "passage" and backTrack == True:
        print("Keep backtracking to the previous junction")
        adviceText = "Keep backtracking to the previous junction"
    if check_if_junction() == "junction":
        # saved as [up info, left info, right info, down info, previous location as number in regard to this array]
        # n=nmark, x=xmark, u=unmarked, w=wall
        junctionInfo = analyse_junction()
        print(junctionInfo)

        if junctionInfo[4] == 0:
            directionFromText = "UP"
        if junctionInfo[4] == 1:
            directionFromText = "LEFT"
        if junctionInfo[4] == 2:
            directionFromText = "RIGHT"
        if junctionInfo[4] == 3:
            directionFromText = "DOWN"

        if (junctionInfo[0] == "u" or junctionInfo[0] == "w") \
                and (junctionInfo[1] == "u" or junctionInfo[1] == "w") \
                and (junctionInfo[2] == "u" or junctionInfo[2] == "w") \
                and (junctionInfo[3] == "u" or junctionInfo[3] == "w"):
            print("New junction, mark ", directionFromText, " RED")
            adviceText = "New junction, mark " + directionFromText + " RED"
        # if unmoved == True

        if (junctionInfo[junctionInfo[4]]) == "x" and junctionInfo[0] != "n" \
                and junctionInfo[1] != "n" and junctionInfo[2] != "n" and junctionInfo[3] != "n":
            print("Mark a new passage GREEN")
            adviceText = "Mark a new passage GREEN"

        if (junctionInfo[junctionInfo[4]]) == "x" and (junctionInfo[0] == "n" \
                                                       or junctionInfo[1] == "n" or junctionInfo[2] == "n" or
                                                       junctionInfo[3] == "n"):
            if junctionInfo[0] == "n":
                text = "UP"
            if junctionInfo[1] == "n":
                text = "LEFT"
            if junctionInfo[2] == "n":
                text = "RIGHT"
            if junctionInfo[3] == "n":
                text = "DOWN"
            print("Take newly marked passage ", text)
            adviceText = "Take newly marked passage " + text

        if junctionInfo[junctionInfo[4]] == "u" \
                and ((junctionInfo[0] == "x" or junctionInfo[0] == "n") \
                     or (junctionInfo[1] == "x" or junctionInfo[1] == "n") \
                     or (junctionInfo[2] == "x" or junctionInfo[2] == "n") \
                     or (junctionInfo[3] == "x" or junctionInfo[3] == "n")):
            print("Old junction reached, mark " + directionFromText + " passage GREEN")
            adviceText = "Old junction reached, mark " + directionFromText + " passage GREEN"

        if backTrack == False and junctionInfo[junctionInfo[4]] == "n" \
                and (junctionInfo[0] == "x" or "n" or "w") \
                and (junctionInfo[0] == "x" or "n" or "w") \
                and (junctionInfo[0] == "x" or "n" or "w") \
                and (junctionInfo[0] == "x" or "n" or "w"):
            print("Backtrack ", directionFromText, " to last junction")
            adviceText = "Backtrack " + directionFromText + " to last junction"

        print(backTrack)
        # print(nMarkList[len(nMarkList)-1])
        print([surroundingCoords[5], surroundingCoords[4]])
        if backTrack and junctionInfo[junctionInfo[4]] == "n":
            if nMarkList[len(nMarkList) - 1] == ([surroundingCoords[1], surroundingCoords[4]]) and junctionInfo[4] != 0:
                print("Traverse UP through new passage")
                adviceText = "Traverse UP through new passage"
            elif nMarkList[len(nMarkList) - 1] == ([surroundingCoords[3], surroundingCoords[4]]) and junctionInfo[
                4] != 1:
                print("traverse LEFT through new passage")
                adviceText = "traverse LEFT through new passage"
            elif nMarkList[len(nMarkList) - 1] == ([surroundingCoords[5], surroundingCoords[4]]) and junctionInfo[
                4] != 2:
                print("traverse RIGHT through new passage")
                adviceText = "traverse RIGHT through new passage"
            elif nMarkList[len(nMarkList) - 1] == ([surroundingCoords[7], surroundingCoords[4]]) and junctionInfo[
                4] != 3:
                print("traverse DOWN through new passage")
                adviceText = "traverse DOWN through new passage"
            elif junctionInfo[0] == "u" or junctionInfo[1] == "u" or junctionInfo[2] == "u" or junctionInfo[3] == "u":
                print("backtracked to junction, mark a new passage GREEN")
                adviceText = "Backtracked to junction, mark a new passage GREEN"
            else:
                if junctionInfo[0] == "x":
                    text = "UP"
                if junctionInfo[1] == "x":
                    text = "LEFT"
                if junctionInfo[2] == "x":
                    text = "RIGHT"
                if junctionInfo[3] == "x":
                    text = "DOWN"
                print("Backtrack ", text, " through the passage marked RED")
                adviceText = "Backtrack " + text + " through the passage marked RED"

    label_current_advice.config(text=adviceText)


def print_goal():
    global goalPosition
    goalTurtle.clearstamps()
    for i in range(len(surroundingCoords)):
        if surroundingCoords[i] == goalPosition:
            goalTurtle.goto(cellposition[i])
            goalTurtle.stamp()


def check_if_at_goal():
    global pxpos
    global pypos
    global goalPosition
    if (pxpos, pypos) == goalPosition:
        print("goal reached")
        enter_compare()


def update_pos(newx, newy):
    global pxpos
    global pypos
    pxpos = newx
    pypos = newy
    print(pxpos)
    print(pypos)
    check_if_backtrack()
    update_position_history()
    update_surounding_coords()
    draw_surroundings()
    print_marks()
    update_cells_travelled_label()
    update_advice()
    print_goal()
    print(backTrack)
    check_if_at_goal()

    # update_marks()
    # if check_if_junction() == "junction":
    # print('at a junction')
    # update_known_junction


def identify_direction(x, y):
    global cellSize
    print(x, y)
    print(cellposition[1])
    print(cellSize)
    if (x > cellposition[1][0] - cellSize / 2) \
            and (x < cellposition[1][0] + cellSize / 2) \
            and (y > cellposition[1][1] - cellSize / 2) \
            and (y < cellposition[1][1] + cellSize / 2):
        print('up pressed')
        cellClicked = 'up'
    elif (x > cellposition[3][0] - cellSize / 2) \
            and (x < cellposition[3][0] + cellSize / 2) \
            and (y > cellposition[3][1] - cellSize / 2) \
            and (y < cellposition[3][1] + cellSize / 2):
        print('left pressed')
        cellClicked = 'left'
    elif (x > cellposition[5][0] - cellSize / 2) \
            and (x < cellposition[5][0] + cellSize / 2) \
            and (y > cellposition[5][1] - cellSize / 2) \
            and (y < cellposition[5][1] + cellSize / 2):
        print('right pressed')
        cellClicked = 'right'
    elif (x > cellposition[7][0] - cellSize / 2) \
            and (x < cellposition[7][0] + cellSize / 2) \
            and (y > cellposition[7][1] - cellSize / 2) \
            and (y < cellposition[7][1] + cellSize / 2):
        print('down pressed')
        cellClicked = 'down'
    else:
        cellClicked = 'invalid'
    return cellClicked


def place_goal():
    global goalPosition
    for i in range(len(mazeArray)):
        for j in range(len(mazeArray[i])):
            character = mazeArray[i][j]
            if character == "3":
                goalPosition = (i, j)


def setup(maze):
    global mazeArray
    global totalCellsTravelled
    global backTrack
    global pxpos
    global pypos
    global cellSize
    global goalPosition
    backTrack = False
    pxpos = 0
    pypos = 0
    cellSize = 0
    totalCellsTravelled = 0
    mazeArray = maze
    travelledCellsNotCurrentRoute.clear()
    positionHistoryList.clear()
    wallsList.clear()
    xMarkList.clear()
    nMarkList.clear()
    markOrderList.clear()
    # xMarkList = []  # stored as (mark position, related junction)
    # nMarkList = []  # stored as (mark position, related junction)
    # wallsList = []
    create_walls_list()
    set_cell_positions()
    place_player()
    place_goal()
    update_surounding_coords()
    draw_surroundings()


def f_pressed():
    enter_compare()


global goalPosition
global totalCellsTravelled
global backTrack
global pxpos
global pypos
global cellSize
InPlay = True
goalPosition = (0, 0)
backTrack = False
pxpos = 0
pypos = 0
cellSize = 0
surroundingCoords = [0, 0, 0, 0, 0, 0, 0, 0, 0]
cellposition = [0, 0, 0, 0, 0, 0, 0, 0, 0]
totalCellsTravelled = 0
mazeArray = []
levels = []
travelledCellsNotCurrentRoute = []
positionHistoryList = []
markOrderList = []
xMarkList = []  # stored as (mark position, related junction)
nMarkList = []  # stored as (mark position, related junction)
wallsList = []

levels.append(level_1)
setup_array(levels[0])
defaultMaze = mazeArray
# levels.append(level_1)
# setup_array(levels[0])
# create_walls_list()
# set_cell_positions()
# place_player()
# update_surounding_coords()
# draw_surroundings()

# setupUI()
setup(mazeArray)

# key commands
frame_turtle.focus_set()
root.bind('<Up>', lambda i: up_pressed())
root.bind('<Down>', lambda i: down_pressed())
root.bind('<Left>', lambda i: left_pressed())
root.bind('<Right>', lambda i: right_pressed())
root.bind('<x>', lambda i: x_pressed())
root.bind('<n>', lambda i: n_pressed())
root.bind("<Button-1>", mouse_click_left)
root.bind("<Button-3>", mouse_click_right)
root.bind('<f>', lambda i: f_pressed())

root.mainloop()
