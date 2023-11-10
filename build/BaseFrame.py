from tkinter import *
import tkinter.messagebox
from build import UsedHardware
from Muse import MuseOscConnection
from eye_movement_tracker import eye_movement_file
from build import Global
from build import page1
from build.page1 import Frame1
from build.page1 import Frame2
from build.page1 import Frame3
import threading

class BaseWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("BaseWindow")
        self.window.configure(bg = Global.variables.background_color)
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (width, height))

        self.frame1 = Frame1(self.window, self)
        self.frame2 = Frame2(self.window, self)
        self.frame3 = Frame3(self.window, self)

        self.current_frame = self.frame1
        self.show_frame(self.frame1)

        self.current_frame = self.frame1

        self.thread_eye_tracker = threading.Thread(target=self.run_eye_tracker)
        self.thread_muse_inputs = threading.Thread(target=self.run_muse_inputs)

        self.window.mainloop()

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide the current frame
        frame.pack()  # Show the selected frame
        self.current_frame = frame
        self.start_threads()


    def start_threads(self):
        # Create and start the first thread for run_eye_tracker
        if page1.Frame1.isCameraUsed and not self.thread_eye_tracker.is_alive():    #I NEED TO CHECK HERE IF THE THREAD IS ALREADY RUNNING
            self.thread_eye_tracker.start()

        # Create and start the second thread for run_muse_inputs
        if page1.Frame1.isMuseUsed and not self.thread_muse_inputs.is_alive():     #I NEED TO CHECK HERE IF THE THREAD IS ALREADY RUNNING
            self.thread_muse_inputs.start()

    def stop_threads(self):
        # Stop existing threads if they are running
        if self.thread_eye_tracker and self.thread_eye_tracker.is_alive():
            self.thread_eye_tracker.join()

        if self.thread_muse_inputs and self.thread_muse_inputs.is_alive():
            self.thread_muse_inputs.join()

    def run_eye_tracker(self):
        UsedHardware.SharedData.update_values()
        eye_track = eye_movement_file.EyeTracker()
        eye_track.eye_track(page1.Frame1.isCameraUsed, UsedHardware.SharedData.isMuseUsed, UsedHardware.SharedData.isEyeTrackingUsed)

    def run_muse_inputs(self):
        muse_inputs = MuseOscConnection.MuseInput()
        muse_inputs.jaw_clench(MuseOscConnection.MuseInput.dispatcher, MuseOscConnection.MuseInput.ip, MuseOscConnection.MuseInput.port, MuseOscConnection.MuseInput.jaw_clench_handler)

if __name__ == "__main__":

    app = BaseWindow()