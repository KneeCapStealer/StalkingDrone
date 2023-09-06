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
        self.tracking_thread = custom_threads.LoopThread(self._tracking_func)
        self.WASD_thread = custom_threads.LoopThread(self._WASD_func)

    def WASD_control(self):
        pass

    def tracking_control(self):
        pass

    def _tracking_func(self):
        pass

    def _WASD_func(self):
        pass