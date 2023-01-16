from EventHandler import EventHandler
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.resize(100, 20)

        self.button1 = QPushButton("1")
        button2 = QPushButton("2")
        button2.clicked.connect(self.the_button_was_clicked)

        box = QHBoxLayout()
        box.addWidget(self.button1)
        box.addWidget(button2)

        self.setLayout(box)

        self.bot = EventHandler()

    def the_button_was_clicked(self):
        print("Clicked!")
        #self.bot.move_from_inventory()
