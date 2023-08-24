from djitellopy import Tello
import keyboard


def WASD_control(tello: Tello, speed: int, rotation_speed: int, up_down_speed: int):
    if keyboard.is_pressed('w'):
        tello.move_forward(speed)

    if keyboard.is_pressed('a'):
        tello.rotate_counter_clockwise(rotation_speed)

    if keyboard.is_pressed('s'):
        tello.move_back(speed)

    if keyboard.is_pressed('d'):
        tello.rotate_clockwise(rotation_speed)

    if keyboard.is_pressed('up arrow'):
        tello.move_up(up_down_speed)

    if keyboard.is_pressed('left arrow'):
        tello.move_left(speed)

    if keyboard.is_pressed('down arrow'):
        tello.move_down(up_down_speed)

    if keyboard.is_pressed('right arrow'):
        tello.move_right(speed)
