import cv2
import mediapipe

cam = cv2.VideoCapture(0)                               # this gets the first video capture device connected to machine (camera)
face_mesh = mediapipe.solutions.face_mesh.FaceMesh()

while True:                                             # infinete loop to keep the camera keep running
    _,frame = cam.read()                                # gets camera input
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # this is turns the video into another color space
    output = face_mesh.process(rgb_frame)               # creates output from rgb_frame (required for face landmarks)
    landmark_points = output.multi_face_landmarks
    print(landmark_points)
    cv2.imshow('Eye Controlled Mouse', frame)   # creates a window to show video captures
    cv2.waitKey(1)