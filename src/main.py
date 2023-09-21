from djitellopy import Tello
import pygame as pg
import record
import UI
from droneController import DroneController


def main():
    print("Started program")
    screen = pg.display.set_mode([1056, 792])

    print("Created screen")
    clock = pg.time.Clock()
    FPS = 60

    IMAGETakeoffDrone = pg.image.load("../pictures/Icons/Drone_takeoff.png")
    IMAGELandDrone = pg.image.load("../pictures/Icons/Drone_land.png")
    IMAGEManuelMode = pg.image.load("../pictures/Icons/Manuel_mode.png")

    clock.tick(FPS)
    pg.init()

    tello = Tello()
    tello.connect()

    frame_read = record.init_recording(tello)

    droneController = DroneController(tello, frame_read)

    takeOffButton = UI.Button(screen, "Take off", IMAGETakeoffDrone, 100, 100, 100, 100, droneController.start_drone)
    landButton = UI.Button(screen, "Land", IMAGELandDrone, 300, 100, 100, 100, droneController.stop_drone)
    trackButton = UI.Button(screen, "Track", IMAGEManuelMode, 300, 250, 100, 100, droneController.start_tracking)


    running = True
    while running:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    running = False

        # get video feed and render it to pygame
        screen.blit(record.frame_read_2_surface(frame_read), (0, 0))
        takeOffButton.draw()
        landButton.draw()
        trackButton.draw()
        UI.draw_target_box(screen, droneController.get_current_targets()[0], 0)

        # time_since_program_launch()
        UI.draw_user_interface(screen)
        UI.render_text(screen, str(tello.get_battery()), 100, 500, 32)

        # Check for button presses
        takeOffButton.update(events)
        landButton.update(events)
        trackButton.update(events)

        pg.display.update()

    tello.streamoff()
    tello.end()


def time_since_program_launch():
    print(float(pg.time.get_ticks() / 1000))


if __name__ == '__main__':
    main()
    pg.quit()
