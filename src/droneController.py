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

        self._tracking_index: int = 0
        self._rects: tuple
        self._weights: tuple

        # Drone control branches
        self._tracking_thread = custom_threads.LoopThread(self._tracking_control)
        self._WASD_thread = custom_threads.LoopThread(self._WASD_control)

        self._tracking_thread.daemon = True
        self._WASD_thread.daemon = True

        self._tracking_thread.pause(True)
        self._WASD_thread.pause(True)

        self._tracking_thread.start()
        self._WASD_thread.start()

    def __del__(self):
        self._tracking_thread.stop()
        self._WASD_thread.stop()

    def start_WASD(self):
        self._tracking_thread.pause(True)
        self._WASD_thread.pause(False)

    def start_tracking(self):
        self._WASD_thread.pause(True)
        self._tracking_thread.pause(False)

    def get_current_targets(self):
        return self._rects, self._weights

    def next_target(self):
        self._tracking_index += 1
        self._tracking_index %= len(self._rects)

    def previous_target(self):
        self._tracking_index -= 1
        self._tracking_index %= len(self._rects)

    def set_target(self, index):
        self._tracking_index = index
        self._tracking_index %= len(self._rects)

    def _tracking_control(self):
        pass

    def _track_humans(self):
        Hog = cv2.HOGDescriptor()
        Hog.setSVMDetector(cv2.HOGDescriptor.getDefaultPeopleDetector())

        height, width, _ = self.frame_read.frame.shape
        frame = cv2.resize(self.frame_read.frame, (width, height))
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        self._rects, self._weights = Hog.detectMultiScale(gray_frame, winStride=(4, 4), padding=(4, 4), scale=1.05)

        sorted_rects = list(self._rects)
        sorted_rects.sort(key=lambda x: x[0])
        with self._lock:
            self.tracking_data.x = sorted_rects[self._tracking_index][0]
            self.tracking_data.y = sorted_rects[self._tracking_index][1]
            self.tracking_data.w = sorted_rects[self._tracking_index][2]
            self.tracking_data.h = sorted_rects[self._tracking_index][3]

    def _WASD_control(self):
        pass

