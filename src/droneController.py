import custom_threads
import threading


class DroneController:
    class TrackingData:
        def __init__(self):
            self.x: float = 0
            self.y: float = 0
            self.w: float = 0
            self.h: float = 0

    def __init__(self):
        self.tracking_data: DroneController.TrackingData = DroneController.TrackingData()
        self.lock = threading.Lock()
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
        pass

    def _WASD_control(self):
        pass

