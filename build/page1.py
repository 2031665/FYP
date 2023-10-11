from tkinter import *
from build import page2
from build import UsedHardware


class Page1:
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

        open_page_button = Button(window, text="open new page", command=self.go_page2)
        open_page_button.pack()



    def go_page2(self):
        win = Toplevel()            #allows me to create a page on top of another page
        page2.Page2(win, UsedHardware.SharedData.isCameraUsed, UsedHardware.SharedData.isMuseUsed, UsedHardware.SharedData.isEyeTrackingUsed)            #calling the Page2 on top of Page1
        self.window.withdraw()      #Withdraw the page1
        win.deiconify()

def page():                             #this method makes it easier to control other pages multiple pages can run at the same time, how ever if we withdraw them they will be discarded
    print("test1")
    window = Tk()
    Page1(window)
    window.mainloop()



if __name__ == '__main__':
    page()