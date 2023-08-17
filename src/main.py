import cv2
from djitellopy import Tello

tello = Tello()

tello.connect()

tello.streamon()

frame_read = tello.get_frame_read()

tello.takeoff()

tello.move_up(200)

cv2.imwrite("picture3.png", frame_read.frame)

tello.land()

tello.streamoff()

