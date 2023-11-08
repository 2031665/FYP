from tkinter import *
import tkinter.messagebox
from build import UsedHardware
from page1 import *

class BaseWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("BaseWindow")
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (width, height))
        background_color = "#7C6767"

        self.frame1 = Frame1(self.window)
        # self.frame2 = Frame2(self.window)



        self.window.mainloop()

    def show_frame1(self):
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide the currently displayed frame
        self.frame1.frame1.pack()  # Show frame 1
        self.current_frame = self.frame1.frame1



if __name__ == "__main__":

    app = BaseWindow()