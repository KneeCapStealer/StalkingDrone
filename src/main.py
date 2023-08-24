# Modules
import cv2
from djitellopy import Tello
import keyboard

# Own Scripts
import wasd


def main():
    MOVE_STEPS = 10
    TURN_STEPS = 10
    UP_DOWN_STEPS = 5

    tello = Tello()

    # Main loop
    running = True
    while running:
        wasd.WASD_control(tello, MOVE_STEPS, TURN_STEPS, UP_DOWN_STEPS)  # Control drone using WASD and arrow keys

        if keyboard.is_pressed('esc'):
            running = False


if __name__ == "__main__":
    main()
    quit('Exit_Success')
