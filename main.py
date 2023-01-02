import random
import sys

import pyautogui
import time
import re
import mouse
import keyboard
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton

class PoeBot():
    trade_window_coords = []
    inventory_coords = []
    def __int__(self):
        time.sleep(2)
        # setpos()

        self.load_pos("data/posTrade.txt", self.trade_window_coords)
        self.load_pos("data/posInv.txt", self.inventory_coords)
    def setpos(self):
        time.sleep(3)
        with open("data/pos.txt", "a") as data:
            for i in range(1):
                #print(re.findall("[0-9]+", str(pyautogui.position()))[0] + ',' + re.findall("[0-9]+", str(pyautogui.position()))[1])
                data.write(re.findall("[0-9]+", str(pyautogui.position()))[0] + ',' + re.findall("[0-9]+", str(pyautogui.position()))[1]+"\n")
                #data.write(pyautogui.position())
                print("next" + str(i)   )
                time.sleep(3)


    # def move_from_inventory(self, inventory_coords, target="stash", pos=59):
    def move_from_inventory(self,target="stash", pos=59):
        if target == "stash":
            self.open_stash()
        keyboard.press("ctrl")
        time.sleep(0.1)
        for i in range(pos, -1, -1):
            mouse.move(self.inventory_coords[i][0] + random.randint(-8, 8), self.inventory_coords[i][1] + random.randint(-8, 8), duration=0.015)
            mouse.click("left")
        keyboard.release("ctrl")


    def check_trade_window(self, window_coords):
        for i in range(60):
            mouse.move(window_coords[i][0] + random.randint(-8, 8), window_coords[i][1] + random.randint(-15, 15),duration=0.015)


    def load_pos(self, file_name, coords):
        with open(file_name, "r") as data:
            for line in data:
                coords.append(list(map(int, line[:-1].split(","))))


    def open_stash(self):
        mouse.move(1027 + random.randint(-8, 8), 426 + random.randint(-8, 8), duration=0.015)
        mouse.click("left")


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.bot = PoeBot()
        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")
        self.bot.move_from_inventory()
        print("asd")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:

        app = QApplication(sys.argv)
        mywindow = MainWindow()
        mywindow.show()
        app.exec()
        # move_from_inventory(inventory_coords)
        # check_trade_window(trade_window_coords)

    except KeyboardInterrupt:
        print('s')

#
#
