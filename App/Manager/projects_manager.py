from file_locations import *

def print_dict_items(dict):
    for key, value in dict.items():
        print(">", key, ":", value)

class ProjectsFolderSetUp:
    FOLDER_NAME = "Projects"  # Name of the folder
    PROJECTS_FOLDER_DIRECTORY = ""
    projects_dict = {}

    project_names_list = []

    def __init__(self, folder_name="Projects"):
        self.FOLDER_NAME = folder_name
        self.check_project_folder_existence(self.FOLDER_NAME)
        self.check_projects_structure(self.project_names_list)

        print_dict_items(self.projects_dict)

    def check_project_folder_existence(self, folder_name):
        try:
            folder_dir = get_folder_path(folder_name)
            self.PROJECTS_FOLDER_DIRECTORY = folder_dir
            print("Projects Directory: ", folder_dir)
            self.enum_projects()
        except NotADirectoryError:
            correct_directory_name = os.path.join(APPLICATION_DIRECTORY, folder_name)
            os.makedirs(correct_directory_name)
            self.PROJECTS_FOLDER_DIRECTORY = correct_directory_name
            self.enum_projects()

    def check_projects_structure(self, projects_names):
        for project_name in projects_names:
            project_dir = self.PROJECTS_FOLDER_DIRECTORY + "/" + project_name

            try:
                img_dir = get_folder_path_specific_dir("Images", project_dir)
            except NotADirectoryError:
                correct_img_dir = os.path.join(project_dir, "Images")
                os.makedirs(correct_img_dir, exist_ok=True)

            try:
                vid_dir = get_folder_path_specific_dir("Videos", project_dir)
            except NotADirectoryError:
                correct_vid_dir = os.path.join(project_dir, "Videos")
                os.makedirs(correct_vid_dir, exist_ok=True)

            try:
                aud_dir = get_folder_path_specific_dir("Audio", project_dir)
            except NotADirectoryError:
                correct_aud_dir = os.path.join(project_dir, "Audio")
                os.makedirs(correct_aud_dir, exist_ok=True)

    def enum_projects(self):
        # Check if the folder path is valid before proceeding with creating the dictionary
        if os.path.exists(self.PROJECTS_FOLDER_DIRECTORY) and os.path.isdir(self.PROJECTS_FOLDER_DIRECTORY):
            self.projects_dict = {
                project: get_folder_path_specific_dir(project, self.PROJECTS_FOLDER_DIRECTORY)
                for project in get_projects_names(self.PROJECTS_FOLDER_DIRECTORY)
            }
            self.project_names_list = list(self.projects_dict.keys())
        else:
            exit()

class GetInProject:
    vid_dir, img_dir, aud_dir = "", "", ""
    project_name = ""

    def __init__(self, project_name, project_dir):
        self.project_name = project_name
        self.vid_dir = get_folder_path_specific_dir("Videos", project_dir)
        self.img_dir = get_folder_path_specific_dir("Images", project_dir)
        self.aud_dir = get_folder_path_specific_dir("Audio", project_dir)

    def get_videos(self):
        videos = []
        # Loop through the directory
        for item in os.listdir(self.vid_dir):
            item_path = os.path.join(self.vid_dir, item)
            # Check if it's a directory (project folder)
            if os.path.isfile(item_path):
                videos.append(item)
            else:
                raise FileNotFoundError(f"The video '{item}' does not exist in the {self.vid_dir}.")
        return videos

    def get_images(self):
        images = []
        # Loop through the directory
        for item in os.listdir(self.img_dir):
            item_path = os.path.join(self.img_dir, item)
            # Check if it's a directory (project folder)
            if os.path.isfile(item_path):
                images.append(item)
            else:
                raise FileNotFoundError(f"The image '{self.img_dir}' does not exist in the {self.img_dir}.")
        return images

    def get_audios(self):
        audios = []
        # Loop through the directory
        for item in os.listdir(self.aud_dir):
            item_path = os.path.join(self.aud_dir, item)
            # Check if it's a directory (project folder)
            if os.path.isfile(item_path):
                audios.append(item)
            else:
                raise FileNotFoundError(f"The audio '{item}' does not exist in the {self.aud_dir}.")
        return audios
