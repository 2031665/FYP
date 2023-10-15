from tkinter import *

from build import UsedHardware


class Page1:
    isCameraUsed = None
    isMuseUsed = None
    isEyeTrackerUsed = None
    def __init__(self, window):
        self.window = window
        self.window.resizable(0, 0)
        self.window.configure(bg = "#7C6767")
        self.window.title("page1")

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (width, height))

        button_camera_yes = Button(window, borderwidth=0, highlightthickness=0, command=UsedHardware.SharedData.is_camera_used_yes, relief="flat", text="Yes", font=("Imprima", 24 * -1), justify="center",width=46,height=3)
        button_camera_yes.pack()
        button_camera_no = Button(window, borderwidth=0, highlightthickness=0, command=UsedHardware.SharedData.is_camera_used_no, relief="flat", text="no", font=("Imprima", 24 * -1), justify="center",width=46,height=3)
        button_camera_no.pack()

        button_muse_yes = Button(window, borderwidth=0, highlightthickness=0, command=UsedHardware.SharedData.is_muse_used_yes, relief="flat", text="Yes", font=("Imprima", 24 * -1), justify="center",width=46,height=3)
        button_muse_yes.pack()
        button_muse_no = Button(window, borderwidth=0, highlightthickness=0, command=UsedHardware.SharedData.is_muse_used_no, relief="flat", text="no", font=("Imprima",24*-1), justify="center", width=46,height=3)
        button_muse_no.pack()

        button_eye_tracking_yes = Button(window, borderwidth=0, highlightthickness=0, command=UsedHardware.SharedData.is_eye_tracking_used_yes, relief="flat", text="Yes", font=("Imprima", 24 * -1), justify="center",width=46,height=3)
        button_eye_tracking_yes.pack()
        button_eye_tracking_no = Button(window, borderwidth=0, highlightthickness=0, command=UsedHardware.SharedData.is_eye_tracking_used_no, relief="flat", text="no", font=("Imprima", 24 * -1), justify="center",width=46,height=3)
        button_eye_tracking_no.pack()

        open_page_button = Button(window, text="open new page", command=self.exit_page)
        open_page_button.pack()

    def exit_page(self):
        update_values()
        self.window.withdraw()      #Withdraw the page1
        self.window.destroy()

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