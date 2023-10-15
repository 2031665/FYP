import multiprocessing
import threading
from eye_movement_tracker import eye_movement_file
from build import page1
from build import page2
from Muse import MuseOscConnection
from build import UsedHardware
from tkinter import *

class MainApplication:
        def run_eye_tracker(self):
            UsedHardware.SharedData.update_values()
            eye_track = eye_movement_file.EyeTracker()
            eye_track.eye_track(page1.Page1.isCameraUsed, UsedHardware.SharedData.isMuseUsed, UsedHardware.SharedData.isEyeTrackingUsed)
        def run_gui(self):
            page1.page()
        def run_muse_inputs(self):
            muse_inputs = MuseOscConnection.MuseInput()
            muse_inputs.jaw_clench(MuseOscConnection.MuseInput.dispatcher, MuseOscConnection.MuseInput.ip, MuseOscConnection.MuseInput.port, MuseOscConnection.MuseInput.jaw_clench_handler)
        def main_menu(self):
            page2.Page2(Tk(), UsedHardware.SharedData.isCameraUsed, UsedHardware.SharedData.isMuseUsed,
                        UsedHardware.SharedData.isEyeTrackingUsed)

if __name__ == "__main__":
    main_app = MainApplication()

    process_gui = threading.Thread(target=main_app.run_gui())
    process_gui.start()
    process_gui.join()
    process_menu = threading.Thread(target=main_app.main_menu)
    process_menu.start()

    print(page1.Page1.isCameraUsed)
    if page1.Page1.isCameraUsed:
        process_eye_tracking = threading.Thread(target=main_app.run_eye_tracker)
        process_eye_tracking.start()

    if page1.Page1.isMuseUsed:
        process_muse = threading.Thread(target=main_app.run_muse_inputs)
        process_muse.start()



