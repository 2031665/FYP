from tkinter import *
from PIL import ImageTk, Image
import page1

class Page2:

    def __init__(self, window):
        self.window = window
        self.window.geometry("1440x1024")
        self.window.resizable(0, 0)
        self.window.configure(bg="#7C6767")
        self.window.title("page2")
        self.window.bind("<Button-1>", self.go_page1)



        page_title = Label(self.window, text="Shooter Game Tutorial", font=("Imprima Regular", 40 * -1), bg="#7C6767", fg="#D9D9D9")
        page_title.place(x=516.0, y=87.0)

        shooter_game_photo = Image.open("assets/GamePictures/ShooterGame.png")
        resized_shooter_game_photo = shooter_game_photo.resize((406,388), Image.ADAPTIVE)
        self.newShooterGamePhoto = ImageTk.PhotoImage(resized_shooter_game_photo)
        photo = Label(self.window, image=self.newShooterGamePhoto)
        photo.image = self.newShooterGamePhoto

        photo.place(x=517,y=153)


    def go_page1(self,_):
        win = Toplevel()  # allows me to create a page on top of another page
        page1.Page1(win)  # calling the Page2 on top of Page1
        self.window.withdraw()  # Withdraw the page1
        win.deiconify()
def page():  # this method makes it easier to control other pages multiple pages can run at the same time, how ever if we withdraw them they will be discarded
    window = Tk()
    Page2(window)
    window.mainloop()


if __name__ == '__main__':
    page()