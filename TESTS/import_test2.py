import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import shutil
import os

def copy_file():
    initial_dir = "/home/YOUNES/Desktop/YOUNES/Python Projects/My Editor/Projects/Project1/Images"
    file_path = filedialog.askopenfilename(initialdir=initial_dir)
    if file_path:
        try:
            dest_dir = "/home/YOUNES/Desktop/YOUNES/Python Projects/My Editor/Projects/Project1/Audio"
            # Get the destination path where the file will be copied
            dest_path = os.path.join(dest_dir, os.path.basename(file_path))
            # Copy the file to the destination path
            shutil.copy(file_path, dest_path)
            print(f"File '{os.path.basename(file_path)}' copied successfully to '{dest_dir}'.")
        except Exception as e:
            print("Error copying the file:", e)

# Create the main tkinter window
root = tk.Tk()
root.title("File Copier")

def open_file_dialog():
    initial_dir = "/home/YOUNES/Desktop/YOUNES/Python Projects/My Editor/Projects/Project1/Images"
    file_dialog = tk.Toplevel(root)
    file_dialog.title("Open File")
    file_dialog.resizable(False, False)  # Set the file dialog not resizable
    file_path = filedialog.askopenfilename(parent=file_dialog, initialdir=initial_dir)
    file_dialog.destroy()  # Destroy the file dialog after selection
    if file_path:
        try:
            dest_dir = "/home/YOUNES/Desktop/YOUNES/Python Projects/My Editor/Projects/Project1/Audio"
            # Get the destination path where the file will be copied
            dest_path = os.path.join(dest_dir, os.path.basename(file_path))
            # Copy the file to the destination path
            shutil.copy(file_path, dest_path)
            print(f"File '{os.path.basename(file_path)}' copied successfully to '{dest_dir}'.")
        except Exception as e:
            print("Error copying the file:", e)

# Create a label to display the copied image or the placeholder image
image_label = tk.Label(root)
image_label.pack(padx=10, pady=10)

# Create a button to copy the file
copy_button = tk.Button(root, text="Copy File", command=open_file_dialog)
copy_button.pack(pady=5)

# Run the tkinter main loop
root.mainloop()
