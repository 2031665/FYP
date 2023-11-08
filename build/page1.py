from tkinter import *
import tkinter.messagebox
from build import UsedHardware


class Page1:
    isCameraUsed = None
    isMuseUsed = None
    isEyeTrackerUsed = None
    def __init__(self, window):
        background_color = "#7C6767"
        self.window = window
        self.window.resizable(0, 0)
        self.window.configure(bg = background_color)
        self.window.title("page1")

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (width, height))


        camera_label = Label(window, text="Would you like to use the camera features?", font=("Imprima", 24 * -1), justify="center", bg=background_color)
        camera_label.pack()
        button_camera_yes = Button(window, borderwidth=0, highlightthickness=0, command=lambda: [UsedHardware.SharedData.is_camera_used_yes(), Page1.enable_button(self)], relief="flat", text="Yes", font=("Imprima", 24 * -1), justify="center",width=46,height=3)
        button_camera_yes.pack()
        button_camera_no = Button(window, borderwidth=0, highlightthickness=0, command=lambda: [UsedHardware.SharedData.is_camera_used_no(), Page1.disable_button(self)], relief="flat", text="no", font=("Imprima", 24 * -1), justify="center",width=46,height=3)
        button_camera_no.pack()

        muse_label = Label(window, text="Do you have access to Muse Headband Hardware?", font=("Imprima", 24 * -1), justify="center", bg=background_color)
        muse_label.pack()
        button_muse_yes = Button(window, borderwidth=0, highlightthickness=0, command=UsedHardware.SharedData.is_muse_used_yes, relief="flat", text="Yes", font=("Imprima", 24 * -1), justify="center",width=46,height=3)
        button_muse_yes.pack()
        button_muse_no = Button(window, borderwidth=0, highlightthickness=0, command=UsedHardware.SharedData.is_muse_used_no, relief="flat", text="no", font=("Imprima",24*-1), justify="center", width=46,height=3)
        button_muse_no.pack()

        eye_tracking_label = Label(window, text="Would you like to use the eye tracking feature?", font=("Imprima", 24 * -1), justify="center", bg=background_color)
        eye_tracking_label.pack()
        self.button_eye_tracking_yes = Button(window, borderwidth=0, highlightthickness=0, command=UsedHardware.SharedData.is_eye_tracking_used_yes, relief="flat", text="Yes", font=("Imprima", 24 * -1), justify="center",width=46,height=3, state="disabled")
        self.button_eye_tracking_yes.pack()
        self.button_eye_tracking_no = Button(window, borderwidth=0, highlightthickness=0, command=UsedHardware.SharedData.is_eye_tracking_used_no, relief="flat", text="no", font=("Imprima", 24 * -1), justify="center",width=46,height=3,state="disabled")
        self.button_eye_tracking_no.pack()

        open_page_button = Button(window, text="open new page", command=self.exit_page)
        open_page_button.pack()

        def click():
            global info_pop
            info_pop = Toplevel(window)

        def pop_up_info_camera():
            tkinter.messagebox.showinfo("Welcome to GFG", "East Button clicked")

        def pop_up_info_muse():
            tkinter.messagebox.showinfo("Welcome to GFG", "East Button clicked")

        def pop_up_info_eye_tracker():
            tkinter.messagebox.showinfo("Welcome to GFG", "East Button clicked")

            # Create a Button

    def enable_button(self):
        self.button_eye_tracking_yes.config(state=NORMAL)
        self.button_eye_tracking_no.config(state=NORMAL)
    def disable_button(self):
        self.button_eye_tracking_yes.config(state=DISABLED)
        self.button_eye_tracking_no.config(state=DISABLED)

    def exit_page(self):
        update_values()
        self.window.withdraw()      #Withdraw the page1
        self.window.destroy()
class Frame1:
    def __init__(self, parent):
        self.parent = parent
        self.frame1 = Frame(self.window, bg='gray')
        self.frame1.pack(fill=BOTH, expand=True)

        label = Label(self)
def update_values():
    Page1.isCameraUsed = UsedHardware.SharedData.isCameraUsed
    Page1.isMuseUsed = UsedHardware.SharedData.isMuseUsed
    Page1.isEyeTrackerUsed = UsedHardware.SharedData.isEyeTrackingUsed
    print(Page1.isCameraUsed)

def page():                             #this method makes it easier to control other pages multiple pages can run at the same time, how ever if we withdraw them they will be discarded
    print("test1")
    window = Tk()
    Page1(window)
    window.mainloop()



if __name__ == '__main__':
    page()