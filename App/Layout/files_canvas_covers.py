from App.Function.Image.image_preprocessing import ImageProcessing
import tkinter as tk
from file_locations import get_files_names, get_folder_path_specific_dir
from App.Manager.projects_manager import GetInProject
from PIL import Image, ImageTk


class FilesImages:
    CANVAS = None
    _width, _height, NUM = 0, 0, 1
    project_name, projects_dir, project_directory = "", "", ""
    resized_image, image = "", ""
    FILE_LIST = []  # file names
    min_canvas_width, min_canvas_height = "", ""

    def __init__(self, main_canvas, _width, _height, _dir, project_name, wanted_folder):
        self.CANVAS = main_canvas
        self._width = _width
        self._height = _height
        self.projects_dir = _dir
        self.project_name = project_name
        self.project_directory = get_folder_path_specific_dir(self.project_name, self.projects_dir)
        self.min_canvas_width = (self._width // 5 + 35)
        self.min_canvas_height = (self._height // 3 + 35)

        # canvas = tk.Canvas()
        # canvas.create_image()
        self.update_canvas(wanted_folder)

    def update_canvas(self, wanted_folder):
        files = GetInProject(self.project_name, self.project_directory)
        if wanted_folder == "Videos":
            self.FILE_LIST = files.get_videos()
        elif wanted_folder == "Images":
            self.FILE_LIST = files.get_images()
        elif wanted_folder == "Audio":
            self.FILE_LIST = files.get_audios()
        else:
            raise NameError(f"{wanted_folder} is not a \"FILES\" folder in {self.project_name}")

        print(len(self.FILE_LIST))
        image_list = []  # Temporary list to store the images (actual img)
        i, j, k = 0, 0, 0

        for img_name in self.FILE_LIST:
            self.image = Image.open(self.project_directory + f"/{wanted_folder}/" + img_name)
            self.resized_image = self.image.resize((self.min_canvas_width, self.min_canvas_height), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.resized_image)
            image_list.append(self.image)  # Add the image to the temporary list
            self.CANVAS.create_image(120 + j, 70 + i, image=self.image)
            if k == 3:
                i = i + 140
                j = 0
                k = 0
                self.NUM += 1
            else:
                j += 240
                k += 1

        # Assign the temporary image list to self.FILE_LIST after the loop has finished
        self.FILE_LIST = image_list
        self.CANVAS.configure(scrollregion=(0, 0, self._width,  (self._height // 3 + 50) * self.NUM))
