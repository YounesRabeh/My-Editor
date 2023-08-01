import tkinter as tk
from tkinter import ttk
from random import randint, choice

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Scrolling')

canvas = tk.Canvas(window, bg='white', scrollregion=(0, 0, 2000, 5000))
canvas.pack(expand=True, fill='both')
# mousewheel scrolling
canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 60), "units"))
# scrollbar
scrollbar = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

window.mainloop()
