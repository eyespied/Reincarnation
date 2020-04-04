from tkinter import *


class SplashScreen(Frame):
    def __init__(self, master=None, width=0.6, height=0.4, useFactor=True):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w = (useFactor and ws * width) or width
        h = (useFactor and ws * height) or height
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.master.overrideredirect(True)
        self.lift()

        root.after(3000, lambda: root.destroy())


if __name__ == '__main__':
    root = Tk()
    sp = SplashScreen(root)
    sp.config(bg="red")
    root.wm_attributes("-transparentcolor", 'red')
    logo = PhotoImage(file='images/REINCARNATION.png')

    m = Label(sp, image=logo)
    m.pack(side=TOP, expand=YES)
    m.config(bg="red", justify=CENTER, font=("calibri", 29))
    root.mainloop()
