# Modules
import cv2
import pygame
from djitellopy import Tello
import pygame as pg

# Own Scripts
import wasd


def main():
    pg.init()
    screen = pg.display.set_mode((720, 480), vsync=60)

    MOVE_STEPS = 50
    TURN_STEPS = 50
    UP_DOWN_STEPS = 50

    tello = Tello()
    tello.connect()
    tello.takeoff()

    print(tello.get_battery())

    # Main loop
    running = True
    while running:
        keys_pressed = {
            'w': False,
            'a': False,
            's': False,
            'd': False,
            'up arrow': False,
            'down arrow': False,
            'left arrow': False,
            'right arrow': False,
        }

        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

            elif event.type == pygame.KEYUP:
                match event.key:
                    case pg.K_w:
                        keys_pressed['w'] = True
                    case pg.K_a:
                        keys_pressed['a'] = True
                    case pg.K_s:
                        keys_pressed['s'] = True
                    case pg.K_d:
                        keys_pressed['d'] = True
                    case pg.K_UP:
                        keys_pressed['up arrow'] = True
                    case pg.K_DOWN:
                        keys_pressed['down arrow'] = True
                    case pg.K_RIGHT:
                        keys_pressed['right arrow'] = True
                    case pg.K_LEFT:
                        keys_pressed['left arrow'] = True

        wasd.WASD_control(tello, keys_pressed, MOVE_STEPS, TURN_STEPS, UP_DOWN_STEPS)

    tello.land()


if __name__ == "__main__":
    main()
    pg.quit()
    quit('Exit_Success')
