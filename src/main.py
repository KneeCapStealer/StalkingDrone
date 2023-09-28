import threading

import cv2
from time import sleep
from djitellopy import Tello

# Custom Scripts
import custom_threads
import record
from droneController import DroneController


if __name__ == "__main__":

    tello = Tello()
    tello.connect()

    tello.streamon()
    # tello.takeoff()

    rec = record.Recorder(tello)
    rec.open_live_recording()

    # droneController = DroneController(tello, (800, 300))
    # droneController.start_tracking()

    sleep(20)

    rec.close_live_recording()
    tello.streamoff()
    # tello.land()


