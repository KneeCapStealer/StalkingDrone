import pygame as pg
from djitellopy import  Tello

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
