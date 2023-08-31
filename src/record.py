import time, cv2
from threading import Thread
from djitellopy import Tello
import pygame as pg
import numpy as np


class Recorder:
    def __init__(self, drone: Tello, screen):
        self.drone = drone
        self.__keepRecording = False
        self.frame_read = drone.get_frame_read()
        self.screen = screen
        self.frame_read = drone.get_frame_read()

    def open_live_recording(self):
        self.__keepRecording = True
        recorder = Thread(target=self.video_recorder)
        recorder.start()

    def close_live_recording(self):
        self.__keepRecording = False

    def video_recorder(self):
        while self.__keepRecording:
            frame = self.frame_read.frame

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = np.flipud(frame)

            frame = pg.surfarray.make_surface(frame)
            frame = pg.transform.scale_by(frame, 1.1)
            return frame
