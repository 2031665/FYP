from tkinter import *
from build import page2

class Page1:
    def __init__(self, window):

        self.window = window
        self.window.resizable(0, 0)
        self.window.configure(bg = "#7C6767")
        self.window.title("page1")

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (width, height))

        page_title = Label(self.window, text="Muse Headband Training", font=("Imprima Regular", 40 * -1), bg="#7C6767", fg="#D9D9D9",justify="center")
        page_title.pack(pady=100)


        # BUTTON-1 (SHOOTER GAME)
        button_1 = Button(self.window, borderwidth=0, highlightthickness=0, command=self.go_page2, relief="flat",text="Shooter Game", font=("Imprima", 24 * -1), justify="center", width=46, height=3)
        button_1.pack(pady=50)

        # BUTTON-2 (ANARAM GAME)
        button_2 = Button(self.window, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat",text="Anagram Game", font=("Imprima", 24 * -1),justify="center", width=46, height=3)
        button_2.pack(pady=50)

        # BUTTON-3 (DRAG-AND-DROP GAME)
        button_3 = Button(self.window, borderwidth=0, highlightthickness=0, command=lambda: print("button_3 clicked"), relief="flat",text="Drag-and-Drop Game", font=("Imprima", 24 * -1),justify="center", width=46, height=3)
        button_3.pack(pady=50)

    def go_page2(self):
        win = Toplevel()            #allows me to create a page on top of another page
        page2.Page2(win)            #calling the Page2 on top of Page1
        self.window.withdraw()      #Withdraw the page1
        win.deiconify()

def page():                             #this method makes it easier to control other pages multiple pages can run at the same time, how ever if we withdraw them they will be discarded
    print("test1")
    window = Tk()
    Page1(window)
    window.mainloop()

if __name__ == '__main__':
    page()