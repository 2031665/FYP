import tkinter
from tkinter import *
from PIL import ImageTk, Image
from build import ShooterGamePage

class Page3:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1440x1024")
        self.window.resizable(0, 0)
        self.window.configure(bg="#7C6767")
        self.window.title("page2")




        self.window.bind("<Button-1>", self.go_shooter_game)

        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.width, self.height))



        canvas = tkinter.Canvas(self.window, width=self.width, height=self.height, bg="#7C6767")
        canvas.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)


        page_title = Label(self.window, text="Shooter Game Tutorial", font=("Imprima Regular", 40 * -1), bg="#7C6767", fg="#D9D9D9",justify="center")
        page_title.pack(pady=100)

        shooter_game_photo = Image.open("build/assets/GamePictures/ShooterGame.png")
        resized_shooter_game_photo = shooter_game_photo.resize((406,388), Image.ADAPTIVE)
        self.newShooterGamePhoto = ImageTk.PhotoImage(resized_shooter_game_photo)
        photo = Label(self.window, image=self.newShooterGamePhoto, borderwidth=0)
        photo.image = self.newShooterGamePhoto
        photo.pack()

        instructive_text = Image.open("build/assets/text/instructive_text_shooter.png")
        resized_text = instructive_text.resize((1166,294), Image.ADAPTIVE)
        self.new_instructive_text=ImageTk.PhotoImage(resized_text)
        photo = Label(self.window, image=self.new_instructive_text, borderwidth=0)
        photo.pack(pady=100)
    def go_shooter_game(self,_):
    # allows me to create a page on top of another page
        ShooterGamePage.ShooterGamePage().execute_game()

def page():  # this method makes it easier to control other pages multiple pages can run at the same time, how ever if we withdraw them they will be discarded
    window = Tk()
    Page3(window)
    window.mainloop()
