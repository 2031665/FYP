import cv2
import mediapipe
import pyautogui

class EyeTracker:
    def eye_track(self, isCameraUsed, isMuseUsed, isEyeTrackingUsed):    #need to add the arguments isCameraUsed and isMuseUsed.
        print(f"TEST CAM {isCameraUsed} TEST MUSE {isMuseUsed} TEST EYETRACK {isEyeTrackingUsed}")
        cam = cv2.VideoCapture(0)                                                        # this gets the first video capture device connected to machine (camera)
        face_mesh = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
        screen_width, screen_height = pyautogui.size()                                   # setting up the screen size so that the frame will match the screen size
        while True:                                                                      # infinite loop to keep the camera keep running
            _,frame = cam.read()                                                         # gets camera input
            frame = cv2.flip(frame,1)                                            # flips the camera view vertically so that its gives only the reflection on screen
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)                           # this is turns the video into another color space
            output = face_mesh.process(rgb_frame)                                        # creates output from rgb_frame (required for face landmarks)
            landmark_points = output.multi_face_landmarks
            frame_height, frame_width, _ = frame.shape                                   # getting the frame_height and frame_width
            if landmark_points:
                landmarks = landmark_points[0].landmark                                  # this detects only one face. (the first face that shows on camera)
                mouth = [landmarks[12], landmarks[14]]
                left =[landmarks[145], landmarks[159]]          #145-159
                right = [landmarks[374], landmarks[386]]
                if isEyeTrackingUsed:
                    for landmark in landmarks[473:474]:                                      # every landmark in the list landmarks but we only require the iris landmarks which are [474][478]
                        x = int(landmark.x * frame_width)
                        y = int(landmark.y * frame_height)
                        cv2.circle(frame,(x,y), 3, (0, 255, 0))            #detects the landmarks of the face with green circles
                        screen_x = int(landmark.x * screen_width)
                        screen_y = int(landmark.y * screen_height)
                        #print(screen_x, screen_y)  # test to see if the cursor matches the correct pixels on the computer
                        data = pyautogui.moveTo(screen_x, screen_y)
                    for landmark in mouth:
                        x = int(landmark.x * frame_width)
                        y = int(landmark.y * frame_height)
                        cv2.circle(frame, (x, y), 3, (255, 255, 0))
                    for landmark in left:
                        x = int(landmark.x * frame_width)
                        y = int(landmark.y * frame_height)
                        cv2.circle(frame, (x, y), 3, (0, 255, 255))
                    for landmark in right:
                        x = int(landmark.x * frame_width)
                        y = int(landmark.y * frame_height)
                        cv2.circle(frame, (x, y), 3, (0, 255, 255))
                if isCameraUsed:
                    #print(mouth[0].y - mouth[1].y)
                    if (mouth[0].y - mouth[1].y) < -0.1:
                        print("mouth open")
                        pyautogui.hotkey('win', 'ctrl', 'o')
                        pyautogui.sleep(1)

                    #print((right[0].y - right[1].y)+(left[0].y - left[1].y))
                    if (right[0].y - right[1].y)+(left[0].y - left[1].y) <0.015:
                        print("noclick")
                        pyautogui.sleep(0.2)
                    else:
                        if(right[0].y - right[1].y) < 0.006:
                            pyautogui.rightClick()
                            print("right click")
                            pyautogui.sleep(0.2)
                        if not isMuseUsed:
                            if (left[0].y - left[1].y) < 0.006:
                                pyautogui.leftClick()
                                print("left click")
                                pyautogui.sleep(0.2)
            cv2.imshow('Eye Controlled Mouse', frame)                            # creates a window to show video captures
            cv2.waitKey(1)

# if __name__ == "__main__":
#     Run = EyeTracker()
#     Run.eye_track()