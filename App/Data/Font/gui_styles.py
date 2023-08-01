from tkinter import ttk

class MyStyle:
    def __init__(self):
        # Create a style for the Notebook
        notebook_style = ttk.Style()
        notebook_style.theme_create("custom_notebook", parent="alt", settings={
            "TNotebook.Tab": {
                "configure": {
                    "background": "lightgray",  # Set the background color of the tabs
                    "foreground": "black",      # Set the text color of the tabs
                    "relief": "groove",
                },
                "map": {
                    "background": [("selected", "blue"), ("active", "white")],
                    "foreground": [("selected", "white"), ("active", "black")],
                },
            }
        })

        notebook_style.theme_use("custom_notebook")
