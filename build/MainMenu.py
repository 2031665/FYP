

from pathlib import Path

from tkinter import *
import page2
# Explicit imports to satisfy Flake8



window = Tk()


window.geometry("1440x1024")
window.configure(bg = "#7C6767")





canvas = Canvas(window,bg = "#7C6767", height = 1024, width = 1440, bd = 0, highlightthickness = 0, relief = "ridge")

canvas.place(x = 0, y = 0)

on = PhotoImage(file="assets/dark-light/light.png")
off = PhotoImage(file="assets/GamePictures/ShooterGame.png")
button_color = "#D9D9D9"
text_color = "#000000"
button_mode = True

def customize():
    global button_mode
    global button_color
    global text_color

    if button_mode:
        button.config(image=off, bg="#26242f", activebackground="#26242f")
        canvas.config(bg="#26242f")
        button_color = "#807777"
        text_color = "#FFFFFF"
        button_mode = False

    else:
        button.config(image=on, bg= "#7C6767", activebackground = "#7C6767")
        canvas.config(bg = "#7C6767")
        button_color = "#D9D9D9"
        text_color = "#000000"
        button_mode = True


#BUTTON-1 (SHOOTER GAME)

button_1 = Button( borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat", text="Shooter Game", font=("Imprima",24* -1), bg=button_color)
button_1.place(x=486.0, y=268.0, width=467.0, height=96.0)

#BUTTON-2 (ANARAM GAME)

button_2 = Button( borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat", text="Anagram Game", font=("Imprima",24* -1), bg=button_color)
button_2.place(x=486.0, y=418.0, width=467.0,height=96.0)

#BUTTON-3 (DRAG-AND-DROP GAME)

button_3 = Button(borderwidth=0, highlightthickness=0, command=lambda: print("button_3 clicked"), relief="flat", text="Drag-and-Drop Game", font=("Imprima",24* -1), bg=button_color)
button_3.place(x=486.0, y=568.0, width=467.0, height=96.0)

canvas.create_text(496.0, 116.0, anchor="nw", text="Muse Headband Training", fill="#D9D9D9", font=("Imprima Regular", 40 * -1))



button = Button(window, image=on, bd=0, bg="#7C6767", activebackground="#7C6767",command=customize)
button.place(x=20, y=900)

window.resizable(False, False)
window.mainloop()