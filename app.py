__author__ = "James Clark"
__credits__ = ["James Clark"]
__version__ = "1.0"

# Import necessary libraries
from gui import GUI
import tkinter as tk

#exec(open('splashscreen.py').read())
root = tk.Tk()
run = GUI(root)
root.mainloop()
