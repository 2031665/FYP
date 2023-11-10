import multiprocessing
import threading
from eye_movement_tracker import eye_movement_file
from build import page1
from build import page2
from Muse import MuseOscConnection
from build import UsedHardware
from build import BaseFrame
from tkinter import *

class MainApplication:

        def run_gui(self):
            BaseFrame.BaseWindow()


if __name__ == "__main__":
    main_app = MainApplication()

    process_gui = threading.Thread(target=main_app.run_gui())
    process_gui.start()
    process_gui.join()

    print(page1.Frame1.isCameraUsed)
    print(page1.Frame1.isMuseUsed)
    print(page1.Frame1.isEyeTrackerUsed)




