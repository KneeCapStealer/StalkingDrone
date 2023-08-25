import cv2
from time import sleep
from djitellopy import Tello

# Custom Scripts

import record

tello = Tello()
tello.connect()
tello.streamon()

recorder = record.Recorder(tello)
recorder.open_live_recording()

tello.takeoff()

sleep(15)
tello.land()
tello.streamoff()
quit()
