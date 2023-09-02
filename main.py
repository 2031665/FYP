import multiprocessing
import threading
from eye_movement_tracker import eye_movement_file
from build import page1
class MainApplication:
        def run_eye_tracker(self):
            eye_track = eye_movement_file.EyeTracker()
            eye_track.eye_track()
        def run_gui(self):
            page1.page()


if __name__ == "__main__":
    main_app = MainApplication()

    process_gui = threading.Thread(target=main_app.run_gui)
    process_eye_tracking = threading.Thread(target=main_app.run_eye_tracker)

    process_gui.start()
    process_eye_tracking.start()

    process_gui.join()
    process_eye_tracking.join()

