from djitellopy import Tello
import keyboard


def WASD_control(tello: Tello, speed: int, rotation_speed: int, up_down_speed: int):
    if keyboard.press_and_release('w'):
        print('W')
        tello.move_forward(speed)

    if keyboard.press_and_release('a'):
        print('a')
        tello.rotate_counter_clockwise(rotation_speed)

    if keyboard.press_and_release('s'):
        print('s')
        tello.move_back(speed)

    if keyboard.press_and_release('d'):
        print('d')
        tello.rotate_clockwise(rotation_speed)

    if keyboard.press_and_release('up arrow'):
        print('up arrow')
        tello.move_up(up_down_speed)

    if keyboard.press_and_release('left arrow'):
        print('left arrow')
        tello.move_left(speed)

    if keyboard.press_and_release('down arrow'):
        print('down arrow')
        tello.move_down(up_down_speed)

    if keyboard.press_and_release('right arrow'):
        print('right arrow')
        tello.move_right(speed)
