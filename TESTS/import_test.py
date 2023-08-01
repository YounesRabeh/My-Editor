import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def list_images_in_directory(directory):
    image_extensions = (".png", ".jpg", ".jpeg")
    image_files = [file for file in os.listdir(directory) if file.lower().endswith(image_extensions)]
    return image_files

def add_selected_images():
    selected_indices = images_listbox.curselection()
    if not selected_indices:
        print("No images selected.")
        return

    destination_folder = "/home/YOUNES/Desktop/YOUNES/Python Projects/My Editor/Projects/Project3/Images/"
    for index in selected_indices:
        filename = images_listbox.get(index)
        source_path = os.path.join(initial_dir, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.copy(source_path, destination_path)

    print("Selected images added to the destination folder.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Selector")
    root.geometry("400x400")

    initial_dir = "/home/YOUNES/Pictures/demetrio, matteo, younes/"
    images_list = list_images_in_directory(initial_dir)

    title_label = tk.Label(root, text="Select Images to Copy", font=("Arial", 16, "bold"))
    title_label.pack(pady=20)

    frame = tk.Frame(root, width=350, height=250)  # Adjust the frame size as needed
    frame.pack()

    images_listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE)
    for image in images_list:
        images_listbox.insert(tk.END, image)
    images_listbox.pack(pady=10)

    add_button = ttk.Button(frame, text="Add Selected Images", command=add_selected_images)
    add_button.pack(pady=10)

    root.mainloop()
