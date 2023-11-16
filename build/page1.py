from tkinter import *
import tkinter.messagebox
from build import UsedHardware
from build import TypingGame
from build import Global
from build import ShooterGamePage
from PIL import ImageTk, Image
from tkinter import messagebox



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

        menu_frame = Frame(self,bg=Global.variables.background_color)
        menu_frame.place(x=0,y=0,relwidth=1, relheight=1)

        info_button_image = Image.open("build/assets/buttons/info_button.png")
        resized_info_button_image = info_button_image.resize((149, 140), Image.ADAPTIVE)
        self.new_resized_info_button_image = ImageTk.PhotoImage(resized_info_button_image)
        info_button = Button(self, image=self.new_resized_info_button_image, command=lambda: controller.show_frame(controller.frame4), bg=Global.variables.background_color, activebackground=Global.variables.background_color, borderwidth=0)
        info_button.pack(side=TOP, anchor=E)

        page_title = Label(self, text="Muse Headband Training", font=("Imprima Regular", 40 * -1), bg="#7C6767", fg="#D9D9D9")
        page_title.pack()

        camera_label = Label(self, text="Would you like to use the camera features?", font=("Imprima", 24 * -1), justify="center", bg=Global.variables.background_color)
        camera_label.pack(pady=3)
        button_camera_yes = Button(self, borderwidth=0, highlightthickness=0, command=lambda: [UsedHardware.SharedData.is_camera_used_yes(), Frame1.enable_button(self),  Frame1.update_values(self)], relief="flat", text="Yes", font=("Imprima", 24 * -1), justify="center",width=46,height=3)
        button_camera_yes.pack(pady=5)
        button_camera_no = Button(self, borderwidth=0, highlightthickness=0, command=lambda: [UsedHardware.SharedData.is_camera_used_no(), Frame1.disable_button(self), Frame1.update_values(self)], relief="flat", text="no", font=("Imprima", 24 * -1), justify="center",width=46,height=3)
        button_camera_no.pack(pady=5)

        muse_label = Label(self, text="Do you have access to Muse Headband Hardware?", font=("Imprima", 24 * -1), justify="center", bg=Global.variables.background_color)
        muse_label.pack(pady=3)
        button_muse_yes = Button(self, borderwidth=0, highlightthickness=0, command=lambda: [UsedHardware.SharedData.is_muse_used_yes(), Frame1.update_values(self)], relief="flat", text="Yes", font=("Imprima", 24 * -1), justify="center",width=46,height=3)
        button_muse_yes.pack(pady=5)
        button_muse_no = Button(self, borderwidth=0, highlightthickness=0, command=lambda: [UsedHardware.SharedData.is_muse_used_no(), Frame1.update_values(self)], relief="flat", text="no", font=("Imprima",24*-1), justify="center", width=46,height=3)
        button_muse_no.pack(pady=5)

        eye_tracking_label = Label(self, text="Would you like to use the eye tracking feature?", font=("Imprima", 24 * -1), justify="center", bg=Global.variables.background_color)
        eye_tracking_label.pack(pady=3)
        self.button_eye_tracking_yes = Button(self, borderwidth=0, highlightthickness=0, command=lambda:[UsedHardware.SharedData.is_eye_tracking_used_yes(), Frame1.update_values(self)], relief="flat", text="Yes", font=("Imprima", 24 * -1), justify="center",width=46,height=3, state="disabled")
        self.button_eye_tracking_yes.pack(pady=5)
        self.button_eye_tracking_no = Button(self, borderwidth=0, highlightthickness=0, command=lambda: [UsedHardware.SharedData.is_eye_tracking_used_no(), Frame1.update_values(self)], relief="flat", text="no", font=("Imprima", 24 * -1), justify="center",width=46,height=3,state="disabled")
        self.button_eye_tracking_no.pack(pady=5)

        button = Button(self, text="Continue", font=("Imprima", 24 * -1), command=lambda: controller.show_frame(controller.frame2), width=46, height=3, borderwidth=0)
        button.pack(pady=100)


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

        back_button_image = Image.open("build/assets/buttons/back_button.png")
        resized_back_button_image = back_button_image.resize((149, 140), Image.ADAPTIVE)
        self.new_resized_back_button_image = ImageTk.PhotoImage(resized_back_button_image)
        back_button = Button(self, image=self.new_resized_back_button_image, command=lambda: controller.show_frame(controller.frame1), bg=Global.variables.background_color, activebackground=Global.variables.background_color, borderwidth=0)
        back_button.pack(side=TOP, anchor=W)

        page_title = Label(self, text="Muse Headband Training", font=("Imprima Regular", 40 * -1), bg="#7C6767", fg="#D9D9D9")
        page_title.pack(side=TOP)


        # Frame2.check_image(self, Frame2.values(self, UsedHardware.SharedData.isCameraUsed, UsedHardware.SharedData.isMuseUsed, UsedHardware.SharedData.isEyeTrackingUsed))

        label_camera = Label(self, text=f"camera Boolean Value: {UsedHardware.SharedData.isCameraUsed}", font=("Imprima", 24 * -1), bg="#7C6767")
        label_camera.pack(pady=10)

        # label_camera = Label(self, text=f"camera Boolean Value: ", image=Frame2.check_image(self, Frame1.isCameraUsed),
        #                      font=("Imprima", 24 * -1), bg="#7C6767", compound='right')
        # label_camera.pack(pady=10)

        label_muse = Label(self, text=f"Muse Boolean Value: {UsedHardware.SharedData.isMuseUsed}", font=("Imprima", 24 * -1), bg="#7C6767")
        label_muse.pack(pady=10)

        # label_muse = Label(self, text=f"muse Boolean Value: ", image=Frame2.check_image(self, Frame1.isMuseUsed), font=("Imprima", 24 * -1), bg="#7C6767", compound='right')
        # label_muse.pack(pady=10)

        label_eye_tracker = Label(self, text=f"eye track Boolean Value: {UsedHardware.SharedData.isEyeTrackingUsed}", font=("Imprima", 24 * -1), bg="#7C6767")
        label_eye_tracker.pack(pady=10)

        # label_eye_tracker = Label(self, text=f"eye track Boolean Value: ",image=Frame2.check_image(self, Frame1.isEyeTrackerUsed), font=("Imprima", 24 * -1), bg="#7C6767", compound='right')
        # label_eye_tracker.pack(pady=10)

        # BUTTON-1 (SHOOTER GAME)
        button_1 = Button(self, borderwidth=0, highlightthickness=0, relief="flat",command=lambda: controller.show_frame(controller.frame3), text="Shooter Game", font=("Imprima", 24 * -1), justify="center", width=46, height=3)
        button_1.pack(pady=10)

        # BUTTON-2 (ANARAM GAME)
        button_2 = Button(self, borderwidth=0, highlightthickness=0, command=lambda: controller.show_frame(controller.frame5), relief="flat", text="Anagram Game", font=("Imprima", 24 * -1), justify="center", width=46, height=3)
        button_2.pack(pady=10)

class Frame3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=Global.variables.background_color)
        self.controller = controller

        back_button_image = Image.open("build/assets/buttons/back_button.png")
        resized_back_button_image = back_button_image.resize((149, 140), Image.ADAPTIVE)
        self.new_resized_back_button_image = ImageTk.PhotoImage(resized_back_button_image)
        back_button = Button(self, image=self.new_resized_back_button_image, command=lambda: controller.show_frame(controller.frame2), bg=Global.variables.background_color, activebackground=Global.variables.background_color, borderwidth=0)
        back_button.pack(side=TOP, anchor=W)

        page_title = Label(self, text="Shooter Game Tutorial", font=("Imprima Regular", 40 * -1), bg="#7C6767", fg="#D9D9D9", justify="center")
        page_title.pack()

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

        button = Button(self, text="Continue", font=("Imprima", 24 * -1), command=lambda: self.go_shooter_game(), width=46, height=3, borderwidth=0)
        button.pack()
    def go_shooter_game(self):
        ShooterGamePage.ShooterGamePage().execute_game()

class Frame4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=Global.variables.background_color)
        self.controller = controller

        back_button_image = Image.open("build/assets/buttons/back_button.png")
        resized_back_button_image = back_button_image.resize((149, 140), Image.ADAPTIVE)
        self.new_resized_back_button_image = ImageTk.PhotoImage(resized_back_button_image)
        back_button = Button(self, image=self.new_resized_back_button_image, command=lambda: controller.show_frame(controller.frame1), bg=Global.variables.background_color, activebackground=Global.variables.background_color, borderwidth=0)
        back_button.pack(side=TOP, anchor=W)

        page_title = Label(self, text="Information of Features", font=("Imprima Regular", 40 * -1), bg="#7C6767", fg="#D9D9D9")
        page_title.pack()

        camera_info_label = Label(self, text="What are Camera features? What do they do?", font=("Imprima", 24 * -1), justify="center", bg=Global.variables.background_color)
        camera_info_label.pack(pady=3)

        camera_info_text = Image.open("build/assets/text/camera_info_text.png")
        resized_camera_info_text = camera_info_text.resize((1084, 187), Image.ADAPTIVE)
        self.newCameraInfoText = ImageTk.PhotoImage(resized_camera_info_text)
        photo = Label(self, image=self.newCameraInfoText, borderwidth=0)
        photo.image = self.newCameraInfoText
        photo.pack()

        muse_info_label = Label(self, text="Why need a Muse Headband?", font=("Imprima", 24 * -1), justify="center", bg=Global.variables.background_color)
        muse_info_label.pack(pady=3)

        muse_info_text = Image.open("build/assets/text/muse_info_text.png")
        resized_muse_info_text = muse_info_text.resize((1084, 187), Image.ADAPTIVE)
        self.newMuseInfoText = ImageTk.PhotoImage(resized_muse_info_text)
        photo = Label(self, image=self.newMuseInfoText, borderwidth=0)
        photo.image = self.newMuseInfoText
        photo.pack()

        eye_tracker_info_label = Label(self, text="What is Eye tracking? How it works?", font=("Imprima", 24 * -1), justify="center", bg=Global.variables.background_color)
        eye_tracker_info_label.pack(pady=3)

        eye_tracker_info_text = Image.open("build/assets/text/eye_tracker_info_text.png")
        resized_eye_tracker_text = eye_tracker_info_text.resize((1092, 218), Image.ADAPTIVE)
        self.newEyeTrackerInfoText = ImageTk.PhotoImage(resized_eye_tracker_text)
        photo = Label(self, image=self.newEyeTrackerInfoText, borderwidth=0)
        photo.image = self.newEyeTrackerInfoText
        photo.pack()

class Frame5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=Global.variables.background_color)
        self.controller = controller

        back_button_image = Image.open("build/assets/buttons/back_button.png")
        resized_back_button_image = back_button_image.resize((149, 140), Image.ADAPTIVE)
        self.new_resized_back_button_image = ImageTk.PhotoImage(resized_back_button_image)
        back_button = Button(self, image=self.new_resized_back_button_image, command=lambda: controller.show_frame(controller.frame2), bg=Global.variables.background_color, activebackground=Global.variables.background_color, borderwidth=0)
        back_button.pack(side=TOP, anchor=W)

        page_title = Label(self, text="Typing Game Tutorial", font=("Imprima Regular", 40 * -1), bg="#7C6767", fg="#D9D9D9", justify="center")
        page_title.pack()

        typing_game_photo = Image.open("build/assets/GamePictures/TypingGameImage.png")
        resized_typing_game_photo = typing_game_photo.resize((636, 385), Image.ADAPTIVE)
        self.newTypingGamePhoto = ImageTk.PhotoImage(resized_typing_game_photo)
        photo = Label(self, image=self.newTypingGamePhoto, borderwidth=0)
        photo.image = self.newTypingGamePhoto
        photo.pack()

        instructive_text = Image.open("build/assets/text/instructive_text_typing_game.png")
        resized_text = instructive_text.resize((1187, 162), Image.ADAPTIVE)
        self.new_instructive_text = ImageTk.PhotoImage(resized_text)
        photo = Label(self, image=self.new_instructive_text, borderwidth=0)
        photo.pack(pady=100)

        button = Button(self, text="Continue", font=("Imprima", 24 * -1), command=lambda: self.go_typing_game(), width=46, height=3, borderwidth=0)
        button.pack()

    def go_typing_game(self):
        # allows me to create a page on top of another page
        TypingGame.TypingGame().execute_game()
# def page():                             #this method makes it easier to control other pages multiple pages can run at the same time, how ever if we withdraw them they will be discarded
#     print("test1")
#     window = Tk()
#     Page1(window)
#     window.mainloop()



# if __name__ == '__main__':
#     page()