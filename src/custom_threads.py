import threading


class Thread(threading.Thread):
    def __init__(self, func, *args, **kwargs):

        super().__init__(target= lambda: self._thread_function(func, *args, **kwargs))
        self._pause = threading.Event()
        self._stop = threading.Event()

    def start(self):
        self._stop.clear()
        super().start()

    def stop(self):
        self._stop.set()

    def pause(self, val: bool):
        if val:
            self._pause.set()
        else:
            self._pause.clear()

    def _thread_function(self, func, *args, **kwargs):
        while not self._stop.is_set():
            if self._pause.is_set():
                continue

            func(*args, **kwargs)
