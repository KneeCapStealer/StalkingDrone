import pygame
import pygame as pg
import numpy as np
from djitellopy import Tello

:)
def draw_target_box(screen, rects: tuple, current_target_index: int, target_color=(0, 255, 0), rest_color=(255, 255, 0)):

    for i, rect in enumerate(rects):
        pyrect = pygame.Rect(rect)
        # TODO: surface :)
        screen.blit(pyrect, )


def draw_user_interface(screen):
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


def render_text(screen, text, xPos, yPos, size):
    font = pg.font.Font('freesansbold.ttf', size)
    textWithStuff = font.render(text, True, [0, 0, 0])

    textRect = textWithStuff.get_rect()
    textRect.left = xPos
    textRect.top = yPos

    screen.blit(textWithStuff, textRect)


class Button:
    def __init__(self, screen, text, image, buttonxPos, buttonyPos, width, height, drone):
        super().__init__()
        self.screen = screen
        self.image = image
        self.text = text
        self.rect = pg.Rect(buttonxPos, buttonyPos, width, height)
        self.drone = drone

    def apply_text(self, text):
        font = pg.font.Font('freesansbold.ttf', 13)
        textWithStuff = font.render(text, True, [0, 0, 0])

        textRect = textWithStuff.get_rect()
        textRect.centerx = self.rect.centerx
        textRect.bottom = self.rect.bottom

        self.screen.blit(textWithStuff, textRect)

    def apply_image(self):
        imageWidth = self.image.get_width()

        scaleFactor = self.rect.width / (imageWidth + imageWidth / 2)
        scaledImage = pg.transform.scale_by(self.image, scaleFactor)
        scaledImageWidth = scaledImage.get_width()
        scaledImagexPos = self.rect.centerx - scaledImageWidth / 2
        scaledImageyPos = self.rect.top + (self.rect.width - scaledImageWidth) / 2

        self.screen.blit(scaledImage, [scaledImagexPos, scaledImageyPos])

    def update(self, events, action):
        for event in events:
            if event.type == pg.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    if action == "Take off":
                        print("takeoff")
                        self.drone.takeoff()

                    elif action == "Land":
                        print("land")
                        self.drone.land()

    def draw(self):
        pg.draw.rect(self.screen, [255, 119, 0], self.rect)
        self.apply_text(self.text)
        self.apply_image()
