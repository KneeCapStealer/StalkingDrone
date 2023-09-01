import threading

import cv2
from time import sleep
from djitellopy import Tello

# Custom Scripts
import custom_threads


def func(var1):

    print(var1)


def test(var1, bob, foo):
    print(var1)
    print(bob)
    print(foo)


lock = threading.Lock()

t = custom_threads.LoopThread(test, 'hello', 21, False)
t2 = custom_threads.LoopThread(test, 'oh shied', 55, True)

t2.start()
t.start()
t.pause(True)
t2.stop()
t.stop()