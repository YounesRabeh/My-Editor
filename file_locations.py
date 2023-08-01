import pathlib
import os.path
from tkinter import filedialog
import shutil

APPLICATION_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

# OS:
def get_file_path(file_name):
    current_dir = pathlib.Path(__file__).parent.resolve()
    DATA_file_abs_path = os.path.join(current_dir, file_name)
    return DATA_file_abs_path

def get_folder_path(folder_name=""):
    if folder_name == "":
        current_directory = os.path.abspath(os.getcwd())
    else:
        current_directory = APPLICATION_DIRECTORY
    folder_path = os.path.join(current_directory, folder_name)
    # Check if the folder actually exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return folder_path
    else:
        raise NotADirectoryError(f"The folder {folder_name} does not exist in {current_directory}.")

def get_folder_path_specific_dir(folder_name, _dir):
    folder_path = os.path.join(_dir, folder_name)
    # Check if the folder actually exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return folder_path
    else:
        raise NotADirectoryError(f"The folder {folder_name} does not exist in {_dir}.")

def get_projects_names(directory):
    projects = []
    # Loop through the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        # Check if it's a directory (project folder)
        if os.path.isdir(item_path):
            projects.append(item)
        else:
            raise IsADirectoryError(f"The directory '{directory}' does not exist in the project.")

    return projects

def get_files_names(directory):
    files = []
    # Loop through the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        # Check if it's a file
        if os.path.isfile(item_path):
            files.append(item)
    return files





APP_DIRECTORY = get_folder_path("App")
DATA_DIRECTORY = get_folder_path_specific_dir("Data", APP_DIRECTORY)
TEMPORARY_DIRECTORY = get_folder_path_specific_dir("_temp", DATA_DIRECTORY)
