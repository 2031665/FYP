from tkinter import *
import page2

class Page1:

    def __init__(self, window):
        self.window = window
        self.window.geometry("1440x1024")
        self.window.resizable(0, 0)
        self.window.configure(bg = "#7C6767")
        self.window.title("page1")
        self.window.attribute('-fullscreen', True)

        page_title = Label(self.window, text="Muse Headband Training", font=("Imprima Regular", 40 * -1), bg="#7C6767", fg="#D9D9D9")
        page_title.place(x=496.0,y=116.0)


        # BUTTON-1 (SHOOTER GAME)
        button_1 = Button(self.window, borderwidth=0, highlightthickness=0, command=self.go_page2, relief="flat",text="Shooter Game", font=("Imprima", 24 * -1), )
        button_1.place(x=486.0, y=268.0, width=467.0, height=96.0)

        # BUTTON-2 (ANARAM GAME)
        button_2 = Button(self.window, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat",text="Anagram Game", font=("Imprima", 24 * -1), )
        button_2.place(x=486.0, y=418.0, width=467.0, height=96.0)

        # BUTTON-3 (DRAG-AND-DROP GAME)
        button_3 = Button(self.window, borderwidth=0, highlightthickness=0, command=lambda: print("button_3 clicked"), relief="flat",text="Drag-and-Drop Game", font=("Imprima", 24 * -1), )
        button_3.place(x=486.0, y=568.0, width=467.0, height=96.0)

    def go_page2(self):
        win = Toplevel()            #allows me to create a page on top of another page
        page2.Page2(win)            #calling the Page2 on top of Page1
        self.window.withdraw()      #Withdraw the page1
        win.deiconify()

def page():                             #this method makes it easier to control other pages multiple pages can run at the same time, how ever if we withdraw them they will be discarded
    window = Tk()
    Page1(window)
    window.mainloop()

if __name__ == '__main__':
    page()