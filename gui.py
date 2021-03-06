__author__ = "James Clark"
__credits__ = ["James Clark"]
__version__ = "2.0"

# Import necessary libraries
import os
import signal
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import story


def printToConsole():
    print("Print to Console")


# Prompts the user to close the application, if 'quit; in menu bar is pressed
def closeQuestion():
    msgBox = tk.messagebox.askquestion('Reincarnation', 'Are you sure you want to exit the application?',
                                       icon='warning')
    if msgBox == 'yes':
        os.kill(os.getpid(), signal.SIGINT)
    else:
        pass


def exportStory():
    with open("generated_stories/{}'s Story.txt".format(name), "w") as text_file:
        text_file.write(story.export_story)


class GUI(tk.Frame):
    root = None

    def __init__(self, parent, master=None, width=0.6, height=0.4, useFactor=True):
        tk.Frame.__init__(self, master)

        self.name_text = None
        self.name_box = None
        self.buttonFour = None
        self.chosen_name = None
        self.creditsInfo = None

        self.parent = parent
        # Window dimensions
        CANVAS_HEIGHT = 600
        CANVAS_WIDTH = 900

        # get screen width and height to center the window
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w = (useFactor and ws * width) or width
        h = (useFactor and ws * height) or height
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.parent.iconbitmap('images/favicon.ico')
        self.parent.title("Reincarnation - AI Generated Stories")
        self.parent.maxsize(CANVAS_WIDTH, CANVAS_HEIGHT)
        self.parent.minsize(CANVAS_WIDTH, CANVAS_HEIGHT)

        # Menubar
        menuBar = tk.Menu(self.parent)

        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Save Story", command=exportStory)
        fileMenu.add_command(label="Credits", command=self.credits)
        fileMenu.add_command(label="Quit", command=closeQuestion)
        menuBar.add_cascade(label="File", menu=fileMenu)
        self.parent.config(menu=menuBar)

        # Creates canvas, which is a child of root and sets the size of the window
        canvas = tk.Canvas(self.root, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, bg='#05345C')
        canvas.pack()

        # Background
        self.background_image = Image.open('images/bg.png')
        self.background_imageCopy = self.background_image.copy()
        self.photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(canvas, image=self.photo)
        self.background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Title
        # Creates Frame for Header
        self.header = tk.Frame(self.parent, width=900, height=100, bg="#e4e4e4")
        self.header.place(x=0, y=0, relx=0, rely=0)

        # Title Frame that uses an image
        self.titleImage = Image.open('images/title.png')
        self.titleImageCopy = self.titleImage.copy()
        self.photo_2 = ImageTk.PhotoImage(self.titleImage)
        self.title = tk.Label(self.header, image=self.photo_2, bg='#e4e4e4')
        self.title.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Creates Frame for Generated Text
        self.textBox = tk.Frame(self.parent, width=500, height=400, bg="white", borderwidth=1, relief="solid")
        self.textBox.place(x=190, y=100, relx=0, rely=0)

        # Label for year n
        self.labelYear = tk.Label(self.textBox, text="Press START to begin", font=("Helvetica", 22), width=20,
                                  bg="white")
        self.labelYear.place(x=80, y=10, relx=0, rely=0)

        # Label to place generated text
        self.labelStory = tk.Label(self.textBox, text=current_string, font=10, width=54, bg="white")
        self.labelStory.place(x=3, y=100, relx=0, rely=0)

        # Creates Frame for 1/3 of screen
        self.lowerThirdFrame = tk.Frame(self.parent, width=900, height=100)
        self.lowerThirdFrame.place(x=0, y=500, relx=0, rely=0)

        #  Creates frame for buttons
        self.buttonBar = tk.Frame(self.lowerThirdFrame, width=900, height=100, bg="#dccda2")
        self.buttonBar.place(x=0, y=0, relx=0, rely=0)

        # Generates buttons
        self.buttonOne = tk.Button(self.buttonBar, width=10, height=2, text="Start", font=("Helvetica", 16),
                                   command=self.startStory)
        self.buttonOne.place(in_=self.buttonBar, x=60, y=14, relx=0, rely=0)
        self.buttonTwo = tk.Button(self.buttonBar, width=15, height=2, text="Advance Period", font=("Helvetica", 16),
                                   command=self.updateStory)
        self.buttonTwo.place(in_=self.buttonBar, x=350, y=14, relx=0, rely=0)
        self.buttonThree = tk.Button(self.buttonBar, width=10, height=2, text="Reset", font=("Helvetica", 16),
                                     command=self.resetStory)
        self.buttonThree.place(in_=self.buttonBar, x=705, y=14, relx=0, rely=0)

        # Disables initial buttons if story is not in progress
        if not start_story:
            self.buttonTwo.config(state='disabled')
            self.buttonThree.config(state='disabled')

    # When the 'START' button has been pressed this function is called.
    def startStory(self):
        global start_story, name, nameChosen, counter, current_period, current_string

        # Disables start button
        self.buttonOne.config(state='disabled')

        # If story hasn't started, ask for a character name
        if not start_story:
            # If name hasn't been selected run character name creation:
            if not nameChosen:
                self.labelYear.config(text='')
                text = "Enter your character's name"
                self.name_text = tk.Label(self.parent, text=text, font=("Helvetica", 16),
                                          bg="white")
                self.name_text.place(x=300, y=115, relx=0, rely=0)
                self.name_box = tk.Entry(self.parent, width=20, font=("Helvetica", 16))
                self.name_box.place(x=310, y=200, relx=0, rely=0)

                self.buttonFour = tk.Button(self.parent, width=10, height=2, text="Submit", font=("Helvetica", 16),
                                            command=self.nameUpdate)
                self.buttonFour.place(in_=self.parent, x=370, y=250, relx=0, rely=0)

            # Once name has been chosen destroy the name label and begin the story.
            if nameChosen:
                self.name_text.destroy()

                # Initializes the story
                story.createStory()
                start_story = True

                # Resets Advance Year and Reset buttons to enabled.
                self.buttonTwo.config(state='normal')
                self.buttonThree.config(state='normal')

                # Sets initial period
                counter = 0
                current_period = "Period: " + str(period[counter])

                # Sets initial text for first period
                current_string = story.final[counter]

                # Sets labels to the variables defined above.
                self.labelStory.config(text=current_string)
                self.labelYear.config(text=current_period)

    # If name has been submitted it runs this function that updates the name_text label and destroys several GUI items.
    def nameUpdate(self):
        global name, nameChosen
        nameChosen = True
        name = self.name_box.get()
        self.name_text.config(text="Character Name: " + name + "\n Press 'START' again to begin!")
        self.buttonOne.config(state='normal')
        self.buttonFour.destroy()
        self.name_box.destroy()

    # When user presses Advance Year, this function is run.
    def updateStory(self):
        global counter, current_period, current_string

        # Increments period by one each time button is pressed
        counter += 1
        if period[counter] == 'End':
            self.thanksForPlaying()

        else:
            current_period = "Period: " + str(period[counter])

            # Increments story to the next period.
            current_string = story.final[counter]

            # Changes GUI Labels to represent the period information.
            self.labelStory.config(text=current_string)
            self.labelYear.config(text=current_period)

    # Once story has finished, save the story and show info box.
    def thanksForPlaying(self):

        # Disables buttons
        self.buttonOne.config(state='disabled')
        self.buttonTwo.config(state='disabled')
        self.labelYear.config(text='The End')
        # Displays info box
        tk.messagebox.showinfo('Reincarnation', 'Thanks for playing!\nThe story has been saved.')

        # Saves the story
        exportStory()

    # Resets all variables and labels to default to start generating a new story again.
    def resetStory(self):
        global start_story, name, nameChosen, current_period, current_string

        msgbox = tk.messagebox.askquestion('Reincarnation', 'Are you sure you want to reset?\n', icon='warning')

        if msgbox == 'yes':
            start_story = False
            name = None
            nameChosen = False
            current_period = None
            current_string = None
            story.export_story = ''

            self.labelStory.config(text="")
            self.labelYear.config(text="")
            self.buttonTwo.config(state='disabled')
            self.buttonThree.config(state='disabled')
            self.startStory()
        else:
            pass

    def credits(self):
        global start_story

        if not start_story:
            text = "REINCARNATION \n VERSION: 2.0\n""AUTHOR: JAMES CLARK"
            # Label to place generated text
            self.creditsInfo = tk.Label(self.textBox, text=text, font=10, width=54, bg="white")
            self.creditsInfo.place(x=3, y=300, relx=0, rely=0)
            self.creditsInfo.after(4000, self.creditsInfo.destroy)
        else:
            tk.messagebox.showerror('Reincarnation', 'Error: Story in progress!')


# Declared global variables
current_string = None
current_period = None
period = ['Born', 'Toddler', 'Early Life', 'Teen', 'Young Adult', 'Adult', 'Elderly', 'End']
counter = 0
start_story = False
name = ''
nameChosen = False
