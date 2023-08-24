from djitellopy import Tello
import pygame


def WASD_control(tello: Tello, keysPressed: dict[str, bool], speed: int, rotation_speed: int, up_down_speed: int):
    if keysPressed['w']:
        print('W')
        tello.move_forward(speed)

    if keysPressed['a']:
        print('a')
        tello.rotate_counter_clockwise(rotation_speed)

    if keysPressed['s']:
        print('s')
        tello.move_back(speed)

    if keysPressed['d']:
        print('d')
        tello.rotate_clockwise(rotation_speed)

    if keysPressed['up arrow']:
        print('up arrow')
        tello.move_up(up_down_speed)

    if keysPressed['left arrow']:
        print('left arrow')
        tello.move_left(speed)

    if keysPressed['down arrow']:
        print('down arrow')
        tello.move_down(up_down_speed)

    if keysPressed['right arrow']:
        print('right arrow')
        tello.move_right(speed)
