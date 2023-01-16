import sys
import threading
import traceback

from PyQt6.QtWidgets import QApplication

from FileModificationHandler import FileModified
from MainWindow import MainWindow


def file_modified():
    print("File Modified")
    return False


def check_event_modified():
    file_modified_handler = FileModified(PATH_TO_LOG, file_modified)
    file_modified_handler.start()


if __name__ == "__main__":
    PATH_TO_LOG = r"C:\Program Files (x86)\Steam\steamapps\common\Path of Exile\logs\Client.txt"
    try:
        threading.Thread(target=check_event_modified).start()
        app = QApplication(sys.argv)
        my_window = MainWindow()
        my_window.show()
        app.exec()
    except Exception as e:
        print(traceback.format_exc())