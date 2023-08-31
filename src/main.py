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


t = custom_threads.Thread(test, bob='hello', var1=21, foo=False)

t.start()
t.stop()