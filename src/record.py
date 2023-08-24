import time, cv2
from threading import Thread
from djitellopy import Tello


class Recorder:
    def __init__(self, drone: Tello):
        self.drone = drone
        self.__keepRecording = False
        self.frame_read = drone.get_frame_read()

    def open_live_recording(self):
        self.__keepRecording = True
        recorder = Thread(target=self.__video_recorder)
        recorder.start()

    def close_live_recording(self):
        self.__keepRecording = False

    def __video_recorder(self):
        height, width, _ = self.frame_read.frame.shape

        while self.__keepRecording:
            frame = cv2.resize(self.frame_read.frame, (width, height))
            cv2.imshow('Input', frame)
            c = cv2.waitKey(1)
            if c == 27:
                break
        cv2.destroyAllWindows()
