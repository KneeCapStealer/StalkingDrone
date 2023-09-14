# Python standard libraries
import threading
import numpy as np

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

    class WASDControls:
        def __init__(self):
            self.w: bool = False
            self.a: bool = False
            self.s: bool = False
            self.d: bool = False
            self.up: bool = False
            self.left: bool = False
            self.down: bool = False
            self.right: bool = False

            self.speed_up: bool = False
            self.speed_down: bool = False

    def __init__(self, drone: Tello, camerascreensize: tuple):
        self.tracking_data: DroneController.TrackingData = DroneController.TrackingData()
        self._lock = threading.Lock()
        self.drone = drone
        self.frame_read = drone.get_frame_read()

        self.WASDControls: DroneController.WASDControls = DroneController.WASDControls()

        self.screen_height = camerascreensize[1]
        self.x_mid = camerascreensize[0] / 2
        self.y_mid = camerascreensize[1] / 2
        self.screen_mid = [self.x_mid, self.y_mid]
        self.left_right_velocity = 0
        self.up_down_velocity = 0
        self.forward_backward_velocity = 0
        self.yaw_velocity = 0
        self.speed = 1

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
        self._lock.acquire()
        tracking_rect_center_x = self.tracking_data.x + self.tracking_data.w / 2
        tracking_rect_center_y = self.tracking_data.y + self.tracking_data.h / 2
        tracking_rect_mid = [tracking_rect_center_x, tracking_rect_center_y]

        vector_from_mid = np.array([abs(self.x_mid - tracking_rect_mid[0]), abs(self.y_mid - tracking_rect_mid[1])])
        distance_from_mid = np.linalg.norm(vector_from_mid)

        def inside_center_zone():
            if (tracking_rect_center_x > self.x_mid * 1.1 or
                    tracking_rect_center_x < self.x_mid * 0.9 or
                    tracking_rect_center_y > self.y_mid * 1.1 or
                    tracking_rect_center_y < self.y_mid * 0.9):
                return False
            else:
                return True

        def inside_dead_zone():
            if (tracking_rect_center_x > self.x_mid * 1.2 or
                    tracking_rect_center_x < self.x_mid * 0.8 or
                    tracking_rect_center_y > self.y_mid * 1.2 or
                    tracking_rect_center_y < self.y_mid * 0.8):
                return False
            else:
                return True

        move_by = self.speed * distance_from_mid
        if not inside_center_zone() and inside_dead_zone():
            if tracking_rect_center_x > self.x_mid:
                self.left_right_velocity = move_by
            else:
                self.left_right_velocity = -move_by

            if tracking_rect_center_y > self.y_mid:
                self.up_down_velocity = -move_by
            else:
                self.up_down_velocity = move_by

            if self.tracking_data.h > self.y_mid:
                self.forward_backward_velocity = -move_by
            else:
                self.forward_backward_velocity = move_by
        self._lock.release()

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

