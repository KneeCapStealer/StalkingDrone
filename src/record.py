import cv2
import djitellopy
import custom_threads
from djitellopy import Tello, BackgroundFrameRead
import pygame as pg
import numpy as np


class VideoStream:
    def __init__(self, drone: Tello):
        drone.streamoff()
        drone.streamon()

        self._videoStream = drone.get_frame_read()
        self._currentFrame = self._videoStream.frame
        self.__updaterThread = custom_threads.LoopThread(self.__update_frame_read)
        self.__updaterThread.start()

    def __del__(self):
        self.__updaterThread.stop()

    def get_current_frame(self):
        return self._currentFrame

    def get_current_frame_as_surface(self):
        outFrame = cv2.cvtColor(self._currentFrame, cv2.COLOR_BGR2RGB)
        outFrame = np.rot90(outFrame)
        outFrame = np.flipud(outFrame)

        outFrame = pg.surfarray.make_surface(outFrame)
        return pg.transform.scale_by(outFrame, 1.1)

    def __update_frame_read(self):
        self._currentFrame = self._videoStream.frame

