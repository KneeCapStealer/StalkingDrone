# Modules
import cv2
from djitellopy import Tello
import keyboard

# Own Scripts
import wasd


def main():
    MOVESTEPS = 10
    TURNSTEPS = 10
    UPDOWNSTEPS = 5

    tello = Tello()

    # Main loop
    running = True
    while running:
        wasd.WASD_control(tello, MOVESTEPS, TURNSTEPS, UPDOWNSTEPS)  # Control drone using WASD and arrow keys

        if keyboard.is_pressed('esc'):
            running = False


if __name__ == "__main__":
    main()
    quit('Exit_Success')
