import multiprocessing
import threading
from eye_movement_tracker import eye_movement_file
from build import page1
from Muse import MuseOscConnection
class MainApplication:
        def run_eye_tracker(self):
            eye_track = eye_movement_file.EyeTracker()
            eye_track.eye_track()
        def run_gui(self):
            page1.page()
        def run_muse_inputs(self):
            muse_inputs = MuseOscConnection.MuseInput()
            muse_inputs.jaw_clench(MuseOscConnection.MuseInput.dispatcher, MuseOscConnection.MuseInput.ip, MuseOscConnection.MuseInput.port, MuseOscConnection.MuseInput.jaw_clench_handler)

if __name__ == "__main__":
    main_app = MainApplication()

    process_gui = threading.Thread(target=main_app.run_gui)
    process_eye_tracking = threading.Thread(target=main_app.run_eye_tracker)
    process_muse = threading.Thread(target=main_app.run_muse_inputs)

    process_muse.start()
    process_gui.start()
    process_eye_tracking.start()

    process_muse.join()
    process_gui.join()
    process_eye_tracking.join()

