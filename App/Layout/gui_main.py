import customtkinter as tk
from gui_resources import Info, SetUpWindow, UI
from App.Manager.projects_manager import ProjectsFolderSetUp
from App.Data.Font.gui_styles import MyStyle
from file_locations import get_folder_path_specific_dir

PROJECT_NAME = "Project1"
app = tk.CTk()  # create CTk window
app_style = MyStyle()  # Custom gui ttk style
window_info = Info(app)  # window start info are fields in info
window_set_up = SetUpWindow(app, window_info)  # init the window
projects = ProjectsFolderSetUp()  # Making sure 'Projects' is correctly set up
project_directory = get_folder_path_specific_dir(PROJECT_NAME, projects.PROJECTS_FOLDER_DIRECTORY)  # the directory of the project
window_UI = UI(app, window_info, projects.PROJECTS_FOLDER_DIRECTORY, PROJECT_NAME)  # make the UI


app.mainloop()
