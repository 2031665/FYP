from tkinter import *
from build import page3
from build import TypingGame
from build import UsedHardware

class Page2:
    def __init__(self, window ,isCameraUsed, isMuseUsed, isEyeTrackerUsed):

        self.window = window
        self.window.resizable(0, 0)
        self.window.configure(bg = "#7C6767")
        self.window.title("page1")

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (width, height))

        page_title = Label(self.window, text="Muse Headband Training", font=("Imprima Regular", 40 * -1), bg="#7C6767", fg="#D9D9D9",justify="center")
        page_title.pack(pady=100)

        label_camera = Label(self.window, text=f"camera Boolean Value: {isCameraUsed}")
        label_camera.pack(pady=10)

        label_muse = Label(self.window, text=f"muse Boolean Value: {isMuseUsed}")
        label_muse.pack(pady=10)

        label_eye_tracker = Label(self.window, text=f"eye track Boolean Value: {isEyeTrackerUsed}")
        label_eye_tracker.pack(pady=10)


        # BUTTON-1 (SHOOTER GAME)
        button_1 = Button(self.window, borderwidth=0, highlightthickness=0, command=self.go_page3, relief="flat",text="Shooter Game", font=("Imprima", 24 * -1), justify="center", width=46, height=3)
        button_1.pack(pady=50)

        # BUTTON-2 (ANARAM GAME)
        button_2 = Button(self.window, borderwidth=0, highlightthickness=0, command=self.go_typing_game, relief="flat",text="Anagram Game", font=("Imprima", 24 * -1),justify="center", width=46, height=3)
        button_2.pack(pady=50)

        # BUTTON-3 (DRAG-AND-DROP GAME)
        button_3 = Button(self.window, borderwidth=0, highlightthickness=0, command=lambda: print("button_3 clicked"), relief="flat",text="Drag-and-Drop Game", font=("Imprima", 24 * -1),justify="center", width=46, height=3)
        button_3.pack(pady=50)

        window.mainloop()
        print(f"camera bool {UsedHardware.SharedData.isCameraUsed}")
        print(f"muse bool {UsedHardware.SharedData.isMuseUsed}")
        print(f"eye tracking bool {UsedHardware.SharedData.isEyeTrackingUsed}")
    def go_typing_game(self):
        # allows me to create a page on top of another page
        TypingGame.TypingGame().execute_game()

    def go_page3(self):
        win = Toplevel()            #allows me to create a page on top of another page
        page3.Page3(win)            #calling the Page2 on top of Page1
        self.window.withdraw()      #Withdraw the page1
        win.deiconify()



