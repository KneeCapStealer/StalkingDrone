import cv2
from djitellopy import Tello
import pygame as pg
from record import Recorder
import UI
from droneController import DroneController


def main():
    screen = pg.display.set_mode([1056, 792])

    clock = pg.time.Clock()
    FPS = 60

    IMAGETakeoffDrone = pg.image.load("../pictures/Icons/Drone_takeoff.png")
    IMAGELandDrone = pg.image.load("../pictures/Icons/Drone_land.png")
    IMAGEManuelMode = pg.image.load("../pictures/Icons/Manuel_mode.png")

    clock.tick(FPS)
    pg.init()

    tello = Tello()
    tello.connect()
    tello.streamon()
    record = Recorder(tello, screen)
    record.open_live_recording()

    takeOffButton = UI.Button(screen, "Take off", IMAGETakeoffDrone, 100, 100, 100, 100, tello)
    landButton = UI.Button(screen, "Land", IMAGELandDrone, 300, 100, 100, 100, tello)

    drone_controller = DroneController(tello)

    running = True
    while running:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
                record.close_live_recording()

            elif event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    running = False
                    record.close_live_recording()

        screen.blit(record.video_recorder(), (0, 0))

        # time_since_program_launch()
        UI.draw_user_interface(screen)
        UI.render_text(screen, str(tello.get_battery()), 100, 500, 32)
        takeOffButton.update(events, "Take off")
        takeOffButton.draw()

        landButton.update(events, "Land")
        landButton.draw()

        pg.display.update()

    tello.end()
    tello.streamoff()


def time_since_program_launch():
    print(float(pg.time.get_ticks() / 1000))


if __name__ == '__main__':
    main()
    pg.quit()
