# Import necessary libraries
import tkinter as tk


def printToConsole():
    print("Print to Console")


class GUI(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_user_interface()

    def on_configure(self):
        # update scroll region after starting 'mainloop'
        # when all widgets are in canvas
        self.scrollbar.configure(scrollregion=self.textBox.bbox('all'))

    def initialize_user_interface(self):
        # Create Menu Bar
        self.parent.title("Reincarnation - AI Generated Stories")
        self.parent.maxsize(900, 600)
        self.parent.minsize(900, 600)
        menuBar = tk.Menu(self.parent)
        helpMenu = tk.Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="Help", command=printToConsole)
        helpMenu.add_command(label="Credits", command=printToConsole)
        menuBar.add_cascade(label="About", menu=helpMenu)
        self.parent.config(menu=menuBar)

        # Creates Frame for Header
        self.header = tk.Frame(self.parent, width=900, height=100, bg="green")
        self.header.place(x=0, y=0, relx=0, rely=0)

        # Creates Frame for Generated Text
        self.textBox = tk.Canvas(self.parent, width=500, height=400, bg="white")
        self.textBox.place(x=190, y=100, relx=0, rely=0.01)

        # Creates scroll bar for text frame
        self.scrollbar = tk.Scrollbar(self.parent, command=self.textBox.yview)
        self.scrollbar.place(x=677, y=100, relx=0, rely=0.01)

        self.textBox.configure(yscrollcommand=self.scrollbar.set)
        self.textBox.bind('<Configure>', self.on_configure())

        self.frame = tk.Frame(self.textBox)
        self.textBox.create_window((0, 0), window=self.frame)

        # Creates Frame for Lower Buttons
        self.lowerThirdFrame = tk.Frame(self.parent, width=900, height=100,)
        self.lowerThirdFrame.place(x=0, y=500, relx=0, rely=0)

        self.buttonBar = tk.Frame(self.lowerThirdFrame, width=900, height=100, bg="red")
        self.buttonBar.place(x=0, y=0, relx=0, rely=0.05)

        self.buttonOne = tk.Button(self.buttonBar, height=2, width=25, text="Start", command=printToConsole)
        self.buttonOne.place(in_=self.buttonBar, x=10, y=28, relx=0, rely=0)
        self.buttonTwo = tk.Button(self.buttonBar, height=2, width=25, text="Advance Year", command=printToConsole)
        self.buttonTwo.place(in_=self.buttonBar, x=350, y=28, relx=0, rely=0)
        self.buttonThree = tk.Button(self.buttonBar, height=2, width=25, text="Reset", command=printToConsole)
        self.buttonThree.place(in_=self.buttonBar, x=705, y=28, relx=0, rely=0)


if __name__ == '__main__':
    root = tk.Tk()
    run = GUI(root)
    root.mainloop()
