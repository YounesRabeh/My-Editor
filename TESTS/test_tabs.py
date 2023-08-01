import tkinter as tk
from tkinter import ttk

def create_canvas(parent, bg_color):
    canvas = tk.Canvas(parent, bg=bg_color, width=200, height=150)
    canvas.pack(fill="both", expand=True)
    return canvas

# Create the tkinter window
root = tk.Tk()
root.geometry("400x300")
root.title("Canvas Switching Example")

# Create a Notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Create three canvases and add them to the Notebook tabs
canvas1 = create_canvas(notebook, "red")
canvas2 = create_canvas(notebook, "green")
canvas3 = create_canvas(notebook, "blue")

# Add canvases to the Notebook tabs
notebook.add(canvas1, text="Tab 1")
notebook.add(canvas2, text="Tab 2")
notebook.add(canvas3, text="Tab 3")

# Start the tkinter main loop
root.mainloop()
