__author__ = "James Clark"
__credits__ = ["James Clark"]
__version__ = "1.0"

# Import necessary libraries
from gui import GUI
import tkinter as tk

# exec(open('splashscreen.py').read())
root = tk.Tk()
run = GUI(root)
root.mainloop()

# TODO: Saving information about the story to a list (dict?), so the markov chains can use it in future to improve
#  the story.

# TODO:
#   - Add accidents to story, chance of death increased.
#   - Redesign chance of death to health percentage.
