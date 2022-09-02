import math
import cmath
import random
import time

start_time = time.time()
start_x = random.randrange(0, 10, 1)
start_y = random.randrange(0, 10, 1)
wanted_x = random.randrange(0, 10, 1)
wanted_y = random.randrange(0, 10, 1)
distance = math.sqrt((wanted_x-start_x)**2 + (wanted_y-start_y)**2)

print("Welcome to the game. Move along the coordinate axis to reach the wanted point. If the distance is 0, you win")
print("Start point: (", start_x, ",", start_y, ")")
print("Distance:", distance)
print("--------------------------------------------")

step = 0
while True:
    distance = math.sqrt((wanted_x - start_x) ** 2 + (wanted_y - start_y) ** 2)
    if distance != 0:
        move = input("Choose the direction of movement: ")
    if distance == 0:
        print("success")
        print(step, "steps taken")
        break
    elif move == "left":
        if (start_x - 1) < 0:
            print("wow, you hit the wall!")
        else:
            print("move left")
            start_x = start_x - 1
            distance = math.sqrt((wanted_x - start_x) ** 2 + (wanted_y - start_y) ** 2)
            step = step + 1
        print("Current position: (", start_x, ",", start_y, ")")
        print("Current distance:", distance)
    elif move == "up":
        if (start_y + 1) > 10:
            print("wow, you hit the wall!")
        else:
            print("move up")
            start_y = start_y + 1
            distance = math.sqrt((wanted_x - start_x) ** 2 + (wanted_y - start_y) ** 2)
            step = step + 1
        print("Current position: (", start_x, ",", start_y, ")")
        print("Current distance:", distance)
    elif move == "down":
        if (start_y - 1) < 0:
            print("wow, you hit the wall!")
        else:
            print("move down")
            start_y = start_y - 1
            distance = math.sqrt((wanted_x - start_x) ** 2 + (wanted_y - start_y) ** 2)
            step = step + 1
        print("Current position: (", start_x, ",", start_y, ")")
        print("Current distance:", distance)
    elif move == "right":
        if (start_x + 1) > 10:
            print("wow, you hit the wall!")
        else:
            print("move right")
            start_x = start_x + 1
            distance = math.sqrt((wanted_x - start_x) ** 2 + (wanted_y - start_y) ** 2)
            step = step + 1
        print("Current position: (", start_x, ",", start_y, ")")
        print("Current distance:", distance)
    else:
        print("choose: left, up, down or right")

now_time = time.time()
print("The game lasted", round(abs(start_time - now_time), 2) , "sec")