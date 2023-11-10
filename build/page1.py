from tkinter import *
import tkinter.messagebox
from build import UsedHardware
from build import TypingGame
from build import Global
from build import ShooterGamePage
from PIL import ImageTk, Image



# class Page1:
#     def __init__(self, window):
#         # background_color = "#7C6767"
#         # self.window = window
#         # self.window.resizable(0, 0)
#
#         # self.window.title("page1")
#         #
#         # width = self.window.winfo_screenwidth()
#         # height = self.window.winfo_screenheight()
#         # self.window.geometry("%dx%d" % (width, height))
#         #
#         #
#
#
#         def click():
#             global info_pop
#             info_pop = Toplevel(window)
#
#         def pop_up_info_camera():
#             tkinter.messagebox.showinfo("Welcome to GFG", "East Button clicked")
#
#         def pop_up_info_muse():
#             tkinter.messagebox.showinfo("Welcome to GFG", "East Button clicked")
#
#         def pop_up_info_eye_tracker():
#             tkinter.messagebox.showinfo("Welcome to GFG", "East Button clicked")
#
#             # Create a Button
#

class Frame1(Frame):
    isCameraUsed = None
    isMuseUsed = None
    isEyeTrackerUsed = None
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=Global.variables.background_color)
        self.controller = controller

        camera_label = Label(self, text="Would you like to use the camera features?", font=("Imprima", 24 * -1), justify="center", bg=Global.variables.background_color)
        camera_label.pack()
        button_camera_yes = Button(self, borderwidth=0, highlightthickness=0, command=lambda: [UsedHardware.SharedData.is_camera_used_yes(), Frame1.enable_button(self),  Frame1.update_values(self)], relief="flat", text="Yes", font=("Imprima", 24 * -1), justify="center",width=46,height=3)
        button_camera_yes.pack()
        button_camera_no = Button(self, borderwidth=0, highlightthickness=0, command=lambda: [UsedHardware.SharedData.is_camera_used_no(), Frame1.disable_button(self), Frame1.update_values(self)], relief="flat", text="no", font=("Imprima", 24 * -1), justify="center",width=46,height=3)
        button_camera_no.pack()

        muse_label = Label(self, text="Do you have access to Muse Headband Hardware?", font=("Imprima", 24 * -1), justify="center", bg=Global.variables.background_color)
        muse_label.pack()
        button_muse_yes = Button(self, borderwidth=0, highlightthickness=0, command=lambda: [UsedHardware.SharedData.is_muse_used_yes(), Frame1.update_values(self)], relief="flat", text="Yes", font=("Imprima", 24 * -1), justify="center",width=46,height=3)
        button_muse_yes.pack()
        button_muse_no = Button(self, borderwidth=0, highlightthickness=0, command=lambda: [UsedHardware.SharedData.is_muse_used_no(), Frame1.update_values(self)], relief="flat", text="no", font=("Imprima",24*-1), justify="center", width=46,height=3)
        button_muse_no.pack()

        eye_tracking_label = Label(self, text="Would you like to use the eye tracking feature?", font=("Imprima", 24 * -1), justify="center", bg=Global.variables.background_color)
        eye_tracking_label.pack()
        self.button_eye_tracking_yes = Button(self, borderwidth=0, highlightthickness=0, command=lambda:[UsedHardware.SharedData.is_eye_tracking_used_yes(), Frame1.update_values(self)], relief="flat", text="Yes", font=("Imprima", 24 * -1), justify="center",width=46,height=3, state="disabled")
        self.button_eye_tracking_yes.pack()
        self.button_eye_tracking_no = Button(self, borderwidth=0, highlightthickness=0, command=lambda: [UsedHardware.SharedData.is_eye_tracking_used_no(), Frame1.update_values(self)], relief="flat", text="no", font=("Imprima", 24 * -1), justify="center",width=46,height=3,state="disabled")
        self.button_eye_tracking_no.pack()

        button = Button(self, text="Switch to Frame 2", command=lambda: controller.show_frame(controller.frame2))
        button.pack()

    def enable_button(self):
        self.button_eye_tracking_yes.config(state=NORMAL)
        self.button_eye_tracking_no.config(state=NORMAL)
    def disable_button(self):
        self.button_eye_tracking_yes.config(state=DISABLED)
        self.button_eye_tracking_no.config(state=DISABLED)

    def update_values(self):
        Frame1.isCameraUsed = UsedHardware.SharedData.isCameraUsed
        Frame1.isMuseUsed = UsedHardware.SharedData.isMuseUsed
        Frame1.isEyeTrackerUsed = UsedHardware.SharedData.isEyeTrackingUsed
        print(Frame1.isCameraUsed)
class Frame2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=Global.variables.background_color)
        self.controller = controller

        page_title = Label(self, text="Muse Headband Training", font=("Imprima Regular", 40 * -1), bg="#7C6767", fg="#D9D9D9",justify="center")
        page_title.pack(pady=100)

        label_camera = Label(self, text=f"camera Boolean Value: {UsedHardware.SharedData.isCameraUsed}")
        label_camera.pack(pady=10)

        label_muse = Label(self, text=f"muse Boolean Value: {UsedHardware.SharedData.isMuseUsed}")
        label_muse.pack(pady=10)

        label_eye_tracker = Label(self, text=f"eye track Boolean Value: {UsedHardware.SharedData.isEyeTrackingUsed}")
        label_eye_tracker.pack(pady=10)

        # BUTTON-1 (SHOOTER GAME)
        button_1 = Button(self, borderwidth=0, highlightthickness=0, relief="flat",command=lambda: controller.show_frame(controller.frame3),
                          text="Shooter Game", font=("Imprima", 24 * -1), justify="center", width=46, height=3)
        button_1.pack()

        # BUTTON-2 (ANARAM GAME)
        button_2 = Button(self, borderwidth=0, highlightthickness=0, command=self.go_typing_game, relief="flat",
                          text="Anagram Game", font=("Imprima", 24 * -1), justify="center", width=46, height=3)
        button_2.pack()

        # BUTTON-3 (DRAG-AND-DROP GAME)
        button_3 = Button(self, borderwidth=0, highlightthickness=0, command=lambda: print("button_3 clicked"),
                          relief="flat", text="Drag-and-Drop Game", font=("Imprima", 24 * -1), justify="center",
                          width=46, height=3)
        button_3.pack()

        button = Button(self, text="Switch to Frame 2", command=lambda: controller.show_frame(controller.frame1))
        button.pack()


    def go_typing_game(self):
        # allows me to create a page on top of another page
        TypingGame.TypingGame().execute_game()
class Frame3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=Global.variables.background_color)
        self.controller = controller

        self.bind("<Button-1>", self.go_shooter_game)

        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()


        canvas = tkinter.Canvas(self, width=self.width, height=self.height, bg="#7C6767")
        canvas.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        page_title = Label(self, text="Shooter Game Tutorial", font=("Imprima Regular", 40 * -1), bg="#7C6767", fg="#D9D9D9", justify="center")
        page_title.pack(pady=100)

        shooter_game_photo = Image.open("build/assets/GamePictures/ShooterGame.png")
        resized_shooter_game_photo = shooter_game_photo.resize((406, 388), Image.ADAPTIVE)
        self.newShooterGamePhoto = ImageTk.PhotoImage(resized_shooter_game_photo)
        photo = Label(self, image=self.newShooterGamePhoto, borderwidth=0)
        photo.image = self.newShooterGamePhoto
        photo.pack()

        instructive_text = Image.open("build/assets/text/instructive_text_shooter.png")
        resized_text = instructive_text.resize((1166, 294), Image.ADAPTIVE)
        self.new_instructive_text = ImageTk.PhotoImage(resized_text)
        photo = Label(self, image=self.new_instructive_text, borderwidth=0)
        photo.pack(pady=100)

        button = Button(self, text="Switch to Frame 2", command=lambda: controller.show_frame(controller.frame2))
        button.pack()
    def go_shooter_game(self):
        ShooterGamePage.ShooterGamePage().execute_game()
# def page():                             #this method makes it easier to control other pages multiple pages can run at the same time, how ever if we withdraw them they will be discarded
#     print("test1")
#     window = Tk()
#     Page1(window)
#     window.mainloop()



# if __name__ == '__main__':
#     page()