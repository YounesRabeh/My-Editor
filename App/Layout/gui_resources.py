import customtkinter as tk
from tkinter import Menu, ttk
from files_canvas_covers import FilesImages
from App.Manager.import_manager import *
from PIL import Image, ImageTk
from file_locations import get_folder_path_specific_dir


class Info:
    #DEFAULT:
    SCREEN_WIDTH = 1020
    SCREEN_HEIGHT = 1080

    def __init__(self, _app):
        self.SCREEN_WIDTH = _app.winfo_screenwidth()
        self.SCREEN_HEIGHT = _app.winfo_screenheight()

class SetUpWindow:
    def __init__(self, _app, _inf):
        tk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        tk.set_default_color_theme("blue")
        size = f"{_inf.SCREEN_WIDTH//2}x{_inf.SCREEN_HEIGHT//2}"
        _app.geometry(size)
        _app.title("MY EDITOR")
        _app.attributes('-zoomed', True)  # Set the window to full screen
        _app.minsize(_inf.SCREEN_WIDTH - 200, _inf.SCREEN_HEIGHT - 200)


class UI:
    file_tab_width, file_tab_height = 0, 0
    projects_directory, project_name, project_dir, _APP = "", "", "", ""

    def __init__(self, _app, _inf, _projects_dir, p_name, ):
        #DATA:
        self.file_tab_width = _inf.SCREEN_WIDTH//2
        self.file_tab_height = _inf.SCREEN_HEIGHT//4
        self.projects_directory = _projects_dir
        self.project_name = p_name
        self.project_dir = get_folder_path_specific_dir(p_name, _projects_dir)
        self._APP = _app

        self.VIDEOS = []
        self.IMAGES = []
        self.AUDIOS = []

        # DRAW UI #
        #### TABS:
        self.tabview = ttk.Notebook(self._APP, width=int(_inf.SCREEN_WIDTH/2), height=int(_inf.SCREEN_HEIGHT/2.2),
                                    )
        self.tabview.place(relx=0, rely=0)
        video_tab_name = "\n" + " " * 33 + "VIDEO" + " " * 33 + "\n"
        image_tab_name = "\n" + " " * 33 + "IMAGES" + " " * 33 + "\n"
        audio_tab_name = "\n" + " " * 33 + "AUDIO" + " " * 33 + "\n"
        self.videos_canvas = self.create_canvas(self.tabview)
        self.images_canvas = self.create_canvas(self.tabview)
        self.audios_canvas = self.create_canvas(self.tabview)

        self.tabview.add(self.videos_canvas, text=video_tab_name)
        self.tabview.add(self.images_canvas, text=image_tab_name)
        self.tabview.add(self.audios_canvas, text=audio_tab_name)

        # TAB 1:

        #self.tab_1 = FilesImages(self.videos_canvas, self.file_tab_width,
        #                    self.file_tab_height, self.projects_directory, self.project_name, "Videos")
        self.video_scrollbar = tk.CTkScrollbar(self.videos_canvas, command=self.videos_canvas.yview,
                                               corner_radius=3)
        self.videos_canvas.configure(yscrollcommand=self.video_scrollbar.set)
        self.video_scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

        # TAB 2:
        self.tab_2 = FilesImages(self.images_canvas, self.file_tab_width,
                           self.file_tab_height, self.projects_directory, self.project_name, "Images")
        self.image_scrollbar = tk.CTkScrollbar(self.images_canvas, command=self.images_canvas.yview,
                                               corner_radius=3)
        self.images_canvas.configure(yscrollcommand=self.image_scrollbar.set)
        self.image_scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

        # TAB 3:
        #self.tab_3 = FilesImages(self.audios_canvas, self.file_tab_width,
        #                    self.file_tab_height, self.projects_directory, self.project_name, "Audio")
        self.audio_scrollbar = tk.CTkScrollbar(self.audios_canvas, command=self.audios_canvas.yview,
                                               corner_radius=3)
        self.audios_canvas.configure(yscrollcommand=self.audio_scrollbar.set)
        self.audio_scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

        self.audios_canvas.config(bg="BLACK")

        ########
        # Menu
        def import_files(import_category):
            file_type_dir = get_folder_path_specific_dir(import_category, self.project_dir)
            if import_category == "Videos":
                __import = ImportVideos(file_type_dir)
            elif import_category == "Images":
                __import = ImportImages(file_type_dir)
            elif import_category == "Audio":
                __import = ImportAudio(file_type_dir)
            else:
                raise NameError(f"{import_category} is not a valid import category")

            copy_file_with_file_log(self.project_dir, file_type_dir)
            self.tab_2.update_canvas("Images")

        window_menubar = Menu(_app, background="grey", border=0, relief="flat", tearoff=0)
        _app.config(menu=window_menubar)
        file_menu = Menu(window_menubar, border=0, relief="flat", tearoff=0)
        window_menubar.add_cascade(label="File          ", menu=file_menu)  # add the File menu to the window_menubar
        file_menu.add_command(label='Import', command=lambda: import_files("Images"))
        file_menu.add_command(label='Exit', command=_app.destroy)  # add a menu item to the menu

    def create_canvas(self, parent, bg_color="lightgrey"):
        canvas = tk.CTkCanvas(parent, bg=bg_color, width=self.file_tab_width, height=self.file_tab_height,
                              highlightthickness=0, relief="flat")
        canvas.pack(fill="both", expand=True)
        return canvas
