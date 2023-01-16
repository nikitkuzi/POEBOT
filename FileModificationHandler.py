import os, time, traceback

class FileModified():
    def __init__(self, file_path, callback):
        self.file_path = file_path
        self.callback = callback
        self.last_time_modified = os.path.getmtime(self.file_path)

    def start(self):
        try:
            while True:
                time.sleep(0.5)
                new_modified = os.path.getmtime(self.file_path)
                if new_modified != self.last_time_modified:
                    self.last_time_modified = new_modified
                    if self.callback():
                        break
        except Exception as e:
            print(traceback.format_exc())

