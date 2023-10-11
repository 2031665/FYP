class UserHardware:

    def __init__(self):

        self.window = tk.Tk()
        self.window.resizable(0, 0)
        self.window.configure(bg = "#7C6767")
        self.window.title("page1")

        self.isCameraUsed = False
        self.isMuseUsed = False

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (width, height))




        # BUTTON-YES FOR CAMERA
        button_muse_yes = Button(self.window, borderwidth=0, highlightthickness=0, command=self.set_camera_true, relief="flat",text="YES", font=("Imprima", 24 * -1), justify="center", width=46, height=3)
        button_muse_yes.pack(pady=50)

        # BUTTON-NO FOR CAMERA
        button_muse_no = Button(self.window, borderwidth=0, highlightthickness=0, command=self.set_camera_false, relief="flat",text="NO", font=("Imprima", 24 * -1),justify="center", width=46, height=3)
        button_muse_no.pack(pady=50)
        self.label_camera = Label(self.window, text=f"camera Boolean Value: {self.isCameraUsed}")
        self.label_camera.pack(pady=10)

        # BUTTON-YES FOR MUSE
        button_camera_yes = Button(self.window, borderwidth=0, highlightthickness=0, command=self.set_muse_true, relief="flat",text="YES", font=("Imprima", 24 * -1), justify="center", width=46, height=3)
        button_camera_yes.pack(pady=50)

        # BUTTON-NO FOR MUSE
        button_camera_no = Button(self.window, borderwidth=0, highlightthickness=0, command=self.set_muse_false, relief="flat", text="NO", font=("Imprima", 24 * -1), justify="center", width=46, height=3)
        button_camera_no.pack(pady=50)
        self.label_muse = Label(self.window, text=f"Boolean Value: {self.isMuseUsed}")
        self.label_muse.pack(pady=10)

        self.open_page_button = Button(self.window, text="Open New Page", command=self.open_page1)
        self.open_page_button.pack(pady=10)
    def set_camera_true(self):
        self.isCameraUsed = True
        self.update_label_CAMERA()
    def set_camera_false(self):
        self.isCameraUsed = False
        self.update_label_CAMERA()
    def set_muse_true(self):
        self.isMuseUsed = True
        self.update_label_MUSE()
    def set_muse_false(self):
        self.isMuseUsed = False
        self.update_label_MUSE()

    def get_isCameraUsed(self):
        return self.isCameraUsed
    def get_isMuseUsed(self):
        return self.isMuseUsed

    def update_label_CAMERA(self):                                                     #USED FOR TESTING PURPOSES
        self.label_camera.config(text=f"CAMERA Boolean Value: {self.isCameraUsed}")
    def update_label_MUSE(self):
        self.label_muse.config(text=f"MUSE Boolean Value: {self.isMuseUsed}")
    def open_page1(self):
        win = Toplevel()  # allows me to create a page on top of another page
        page1.Page1(win, self.isCameraUsed, self.isMuseUsed)  # calling the Page2 on top of Page1
        self.window.withdraw()  # Withdraw the page1
        win.deiconify()

def page():                             #this method makes it easier to control other pages multiple pages can run at the same time, how ever if we withdraw them they will be discarded
    window = Tk()
    UserHardware()            #DONT FORGET TO ADD THE OTHER CLASS WITH THE PARAMETER
    window.mainloop()

if __name__ == '__main__':
    page()