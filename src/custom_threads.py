import threading


class LoopThread(threading.Thread):
    """
    This class is an extension of the threading.Thread class.
    Added features include looping the given function.
    A stop and pause function.
    This class will run a function in a loop until stop() is called

    :param func: Function the thread will run parallel in a loop
    :param args: The arguments the function is taking without keywords
    :param kwargs: The arguments the function is taking with keywords
    """
    def __init__(self, func, *args, **kwargs):

        super().__init__(target= lambda: self._thread_function(func, *args, **kwargs))
        self._pause = threading.Event()
        self._stop = threading.Event()

    def start(self):
        self._stop.clear()
        super().start()

    def stop(self):
        """
        Stop the thread.
        Thread will only stop running after it has finished execution.
        It will wait until the finished function is done running.
        """
        self._stop.set()

    def pause(self, val: bool):
        """
        Pause or resume the running of the thread function.
        Nothing will happen if pause() is called multiple times with same parameters.
        :param val: Whether to pause or not ``True: Pause, False: Resume``
        """
        if val:
            self._pause.set()
        else:
            self._pause.clear()

    def _thread_function(self, func, *args, **kwargs):
        while not self._stop.is_set():
            if self._pause.is_set():
                continue

            func(*args, **kwargs)
