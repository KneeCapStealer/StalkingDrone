import cv2
from djitellopy import Tello
import pygame as pg
from record import Recorder
from button import Button

screen = pg.display.set_mode([1056, 792])

clock = pg.time.Clock()
FPS = 60

IMAGETakeoffDrone = pg.image.load("../pictures/Icons/Drone_takeoff.png")
IMAGELandDrone = pg.image.load("../pictures/Icons/Drone_land.png")
IMAGEManuelMode = pg.image.load("../pictures/Icons/Manuel_mode.png")

def main():
    clock.tick(FPS)
    pg.init()


    tello = Tello()
    tello.connect()
    tello.streamon()
    record = Recorder(tello, screen)
    record.open_live_recording()

    takeOffButton = Button(screen, "Take off", IMAGETakeoffDrone    , 100, 100, 100, 100, tello)
    landButton = Button(screen, "Land", IMAGELandDrone, 300, 100, 100, 100, tello)


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

        #time_since_program_launch()
        user_interface()
        text_renderer(str(tello.get_battery()), 100, 500, 32)
        takeOffButton.update(events, "Take off")
        takeOffButton.draw()

        landButton.update(events, "Land")
        landButton.draw()

        pg.display.update()

    tello.end()
    tello.streamoff()




def user_interface():
    orangeColor = [255, 119, 0]
    grayColor = [64, 64, 64]
    greenColor = [60, 255, 60]
    redColor = [255, 60, 60]

    mapRadius = 120
    # Background rect for map
    pg.draw.rect(screen, grayColor, pg.Rect(1056 - mapRadius, 0, mapRadius, mapRadius))
    # Rect containing battery and flight time information
    topInfoPanel = pg.Rect(1056 - mapRadius * 3.25, -mapRadius / 4, mapRadius * 2.5, mapRadius / 2)
    pg.draw.rect(screen, grayColor, topInfoPanel, border_radius=10)
    # Rect for control panel
    pg.draw.rect(screen, orangeColor, pg.Rect(1056 - mapRadius / 2, mapRadius, mapRadius * 2, mapRadius * 3), border_radius=10)
    # Rect for takeoff
    takeoffRect = pg.Rect(1056 - mapRadius / 2, mapRadius * 4.15, mapRadius, mapRadius / 2)
    pg.draw.rect(screen, greenColor, takeoffRect, border_radius=10)
    # Rect for landing
    landingRect = pg.Rect(1056 - mapRadius / 2, mapRadius * 4.75, mapRadius, mapRadius / 2)
    pg.draw.rect(screen, redColor, landingRect, border_radius=10)
    # Outline for map circle
    pg.draw.circle(screen, grayColor, [1056 - mapRadius, mapRadius], mapRadius + 2)
    # Circle for map or other cool stuff
    pg.draw.circle(screen, orangeColor, [1056 - mapRadius, mapRadius], mapRadius)


def text_renderer(text, xPos, yPos, size):
    font = pg.font.Font('freesansbold.ttf', size)
    textWithStuff = font.render(text, True, [0, 0, 0])

    textRect = textWithStuff.get_rect()
    textRect.left = xPos
    textRect.top = yPos

    screen.blit(textWithStuff, textRect)


def time_since_program_launch():
    print(float(pg.time.get_ticks() / 1000))


def battery_info(tello):
    battery = tello.get_battery


if __name__ == '__main__':
    main()
    pg.quit()




