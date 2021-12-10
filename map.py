import random
import numpy

# Sequence that creates the dungeon
s = random.randint(5, 8)   # Allows the layout to change size

dungeon = numpy.arange(s*s).reshape(s,s)   # Creates the layout, can change the reshape to break the "square" rooms
dungeon[0:s] = 0   # Changes the room to a "blank" state


row = random.randint(0, (s-1)) # (size - 1) for indexing purposes
col = random.randint(0, (s-1))

room_status = "start"

in_dungeon = True
while in_dungeon == True:
    print(room_status)  # Using this for testing purposes, displays if the player has visited the room before
    if room_status == "start":
        print("Welcome to the dungeon!")

    if room_status == 1 and movement == True:
        print("You've visited this room already! Nothing happens.")

    if room_status == 0:
        events = [
            "fight",  # 30% chance, event_weight(0)
            "trap",   # 20% chance, event_weight(1)
            "reward", # 10% chance, event_weight(2)
            "neutral" # 40% chance, event_weight(3)
            ]
        event_weight = [.3, .2, .1, .4]

        event_choice = random.choices(events, event_weight, k=1)
        event_trigger = event_choice.pop(0)

        if event_trigger == 'fight':
            print("You enter the next room, entering into combat with a Giant Rat!")
            #Insert battle sequence?
        if event_trigger == "trap":
            print("As you walk into the next room, you sense a tripwire. You sense it, by tripping over it and falling on your face.")
            #Lose 50 health
        if event_trigger == "reward":
            print("You find a chest, gaining 50 gold!")
            #Gain reward
        if event_trigger == "neutral":
            print("You enter the room, look around, and see a dirt floor. Nice.")


    move_up = True
    move_right = True
    move_down = True
    move_left = True
    move = []

    coords = (row, col)

    if row == 0:
        move_left = False
    if col == 0:
        move_up = False
    if row == (s-1):
        move_right = False
    if col == (s-1):
        move_down = False

    if move_up == True:
        move.append("Up")
    if move_down == True:
        move.append("Down")
    if move_left == True:
        move.append("Left")
    if move_right == True:
        move.append("Right")

    # Changes the room back to "Explored" after map is printed
    dungeon[col, row] = 1

    print("You are able to go: ")
    print(*move, sep = ", ")
    move_input = input("Which direction do you want to go? ").lower()


    movement = False
    while movement == False:
        if move_input == "up" and move_up == True:
            col -= 1
            print("You have moved up one room!")
            movement = True
        if move_input == "right" and move_right == True:
            row += 1
            print("You have moved right one room!")
            movement = True
        if move_input == "down" and move_down == True:
            col += 1
            print("You have moved down one room!")
            movement = True
        if move_input == "left" and move_left == True:
            row -= 1
            print("You have moved left one room!")
            movement = True
        if move_input == "quit":                   ###### THIS IS FOR TESTING PURPOSES TO BREAK OUT OF LOOP(even though it isn't a proper shutdown sequence)###### 
            quit()
        if move_input == "map":
            dungeon[col, row] = 2   # Changes the current room (based on current position) to show player position
            print(dungeon)
            print("Legend:")
            print("0 = Unexplored")
            print("1 = Explored")
            print("2 = Player Location")
            print(" ")
            movement = True
        if movement == False:
            print(f'Direction "{move_input}" is not valid. Please choose a valid direction.')
            break

    move_to = (col, row)
    room_status = dungeon[move_to]