from App.Function.Image.image_preprocessing import ImageProcessing
import tkinter as tk
from file_locations import get_files_names, get_folder_path_specific_dir
from App.Manager.projects_manager import GetInProject
from PIL import Image, ImageTk


class FilesImages:
    CANVAS = None
    _width, _height, NUM = 0, 0, 0
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
        self.NUM = 1

        files = GetInProject(self.project_name, self.project_directory)
        if wanted_folder == "Videos":
            self.FILE_LIST = files.get_videos()
        elif wanted_folder == "Images":
            self.FILE_LIST = files.get_images()
        elif wanted_folder == "Audio":
            self.FILE_LIST = files.get_audios()
        else:
            raise NameError(f"{wanted_folder} is not a \"FILES\" folder in {self.project_name}")

        info = "|INFO| Ihe 'Images' folder has: " + str(len(self.FILE_LIST)) + " files"
        print(f"\033[{36}m{info}\033[0m")  # Set the console color to Cyan
        image_list = []  # Temporary list to store the images (actual img)
        i, j, k = 0, 0, 0
        height_adding, row_counter = 0, 0

        for img_name in self.FILE_LIST:
            self.image = Image.open(self.project_directory + f"/{wanted_folder}/" + img_name)
            self.resized_image = self.image.resize((self.min_canvas_width, self.min_canvas_height), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.resized_image)
            image_list.append(self.image)  # Add the image to the temporary list
            self.CANVAS.create_image(120 + j, 70 + i, image=self.image)
            if k == 3:
                i = i + 140            # Y-axis
                j = 0                  # X-axis
                k = 0                  # Column
                row_counter += 1  # Row
            else:
                j += 240
                k += 1

        # TODO: not update --canvas (so big)
        print(self.NUM)
        if row_counter > 3:
            for i in range(row_counter - 3):
                self.NUM += 1
        for i in range(self.NUM):
            height_adding += 5

        # Assign the temporary image list to self.FILE_LIST after the loop has finished
        self.FILE_LIST = image_list
        self.CANVAS.configure(scrollregion=(0, 0, self._width, ((self._height * self.NUM) + 290 + height_adding)))
