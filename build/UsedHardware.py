from build import page1
class SharedData:
    isCameraUsed = False
    isMuseUsed = False
    isEyeTrackingUsed = False

    @classmethod
    def is_camera_used_yes(cls):
        cls.isCameraUsed = True
        print("camera now true")
    @classmethod
    def is_camera_used_no(cls):
        cls.isCameraUsed = False
        print("camera now false")

    @classmethod
    def is_muse_used_yes(cls):
        cls.isMuseUsed = True
        print("muse now true")
    @classmethod
    def is_muse_used_no(cls):
        cls.isMuseUsed = False
        print("muse now false")
    @classmethod
    def is_eye_tracking_used_yes(cls):
        cls.isEyeTrackingUsed = True
        print("eye tracker now true")
    @classmethod
    def is_eye_tracking_used_no(cls):
        cls.isEyeTrackingUsed = False
        print("eye tracker now false")
