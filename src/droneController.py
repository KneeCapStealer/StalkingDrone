# Python standard libraries
import threading

# Imported libraries
from djitellopy import Tello
import cv2

# Own Scripts
import custom_threads


class DroneController:
    class TrackingData:
        def __init__(self):
            self.x: float = 0
            self.y: float = 0
            self.w: float = 0
            self.h: float = 0

    def __init__(self, drone: Tello):
        self.tracking_data: DroneController.TrackingData = DroneController.TrackingData()
        self._lock = threading.Lock()
        self.drone = drone
        self.frame_read = drone.get_frame_read()

        self._rects = 0
        self._weights = 0

        self.tracking_thread = custom_threads.LoopThread(self._tracking_control)
        self.WASD_thread = custom_threads.LoopThread(self._WASD_control)

        self.tracking_thread.daemon = True
        self.WASD_thread.daemon = True

        self.tracking_thread.pause(True)
        self.WASD_thread.pause(True)

        self.tracking_thread.start()
        self.WASD_thread.start()

    def __del__(self):
        self.tracking_thread.stop()
        self.WASD_thread.stop()

    def start_WASD(self):
        self.tracking_thread.pause(True)
        self.WASD_thread.pause(False)

    def start_tracking(self):
        self.WASD_thread.pause(True)
        self.tracking_thread.pause(False)

    def _tracking_control(self):
        pass

    def _track_humans(self):
        Hog = cv2.HOGDescriptor()
        Hog.setSVMDetector(cv2.HOGDescriptor.getDefaultPeopleDetector())

        height, width, _ = self.frame_read.frame.shape
        frame = cv2.resize(self.frame_read.frame, (width, height))
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        self._rects, self._weights = Hog.detectMultiScale(gray_frame, winStride=(4, 4), padding=(4, 4), scale=1.05)

        # TODO: implement switching between targets
        # Currently the best target with the highest score is tracked
        bestWeightIndex = self._weights.index(max(self._weights))

        self._lock.acquire()
        self.tracking_data.x = self._rects[bestWeightIndex][0]
        self.tracking_data.y = self._rects[bestWeightIndex][1]
        self.tracking_data.w = self._rects[bestWeightIndex][2]
        self.tracking_data.h = self._rects[bestWeightIndex][3]
        self._lock.release()



    def _WASD_control(self):
        pass

