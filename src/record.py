import cv2
import custom_threads
from djitellopy import Tello, BackgroundFrameRead
import pygame as pg
import numpy as np


def init_recording(drone: Tello):
    drone.streamoff()
    drone.streamon()
    return drone.get_frame_read()


def frame_read_2_surface(frame_read: BackgroundFrameRead) -> pg.surface:
    frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = np.flipud(frame)

    frame = pg.surfarray.make_surface(frame)
    return pg.transform.scale_by(frame, 1.1)


class Recorder:
    def __init__(self, drone: Tello, screen):
        self.drone = drone



        self.__keepRecording = False

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

            return frame
