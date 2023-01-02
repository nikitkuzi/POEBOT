import random

import pyautogui
import time
import re
import mouse
import keyboard

def setpos():
    time.sleep(3)
    with open("data/pos.txt", "a") as data:
        for i in range(1):
            #print(re.findall("[0-9]+", str(pyautogui.position()))[0] + ',' + re.findall("[0-9]+", str(pyautogui.position()))[1])
            data.write(re.findall("[0-9]+", str(pyautogui.position()))[0] + ',' + re.findall("[0-9]+", str(pyautogui.position()))[1]+"\n")
            #data.write(pyautogui.position())
            print("next" + str(i)   )
            time.sleep(3)


def move_from_inventory(inventory_coords, target="stash", pos=59):
    if target == "stash":
        open_stash()
    keyboard.press("ctrl")
    time.sleep(0.1)
    for i in range(pos, -1, -1):
        mouse.move(inventory_coords[i][0] + random.randint(-8, 8), inventory_coords[i][1] + random.randint(-8, 8), duration=0.015)
        mouse.click("left")
    keyboard.release("ctrl")

def check_trade_window(window_coords):
    for i in range(60):
        mouse.move(window_coords[i][0] + random.randint(-8, 8), window_coords[i][1] + random.randint(-15, 15),duration=0.015)


def load_pos(file_name, coords):
    with open(file_name, "r") as data:
        for line in data:
            print(line)
            coords.append(list(map(int, line[:-1].split(","))))

def open_stash():
    mouse.move(1027 + random.randint(-8, 8), 426 + random.randint(-8, 8), duration=0.015)
    mouse.click("left")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tmp = []
    with open("data/posTrade.txt", "w") as data:
        y = 200 - 27
        #y = 583
        x = 307 - 27
        #x = 1265
        for i in range(12):
            x += 54
            y = 200 - 27
            for j in range(5):
                y += 54
                tmp.append([x, y])
                data.write(str(x) + "," + str(y) + "\n")

    try:
        time.sleep(2)
        # setpos()
        trade_window_coords = []
        inventory_coords = []
        load_pos("data/posTrade.txt", trade_window_coords)
        load_pos("data/posInv.txt", inventory_coords)
        move_from_inventory(inventory_coords)
        # check_trade_window(trade_window_coords)

    except KeyboardInterrupt:
        print('s')

#
#
