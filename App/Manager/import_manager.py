import os
import shutil
from tkinter import filedialog

class ImportVideos:
    directory = ""

    def __init__(self, _dir):
        self.directory = _dir
        pass


def copy_file_with_file_log(initial_dir, destination_dir):
    file_path = filedialog.askopenfilename(initialdir=initial_dir)
    if file_path:
        try:
            destination_path = os.path.join(destination_dir, os.path.basename(file_path))
            shutil.copy(file_path, destination_path)  # Copy the file to the destination path
            print(f"File '{os.path.basename(file_path)}' copied successfully to '{destination_dir}'.")
        except Exception as e:
            raise FileNotFoundError("Error copying the file:", e)


class ImportImages:
    directory = ""

    def __init__(self, _dir):
        self.directory = _dir


class ImportAudio:
    directory = ""

    def __init__(self, _dir):
        self.directory = _dir
        pass

