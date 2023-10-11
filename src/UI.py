import pygame
import pygame as pg


def draw_target_box(screen, rects: tuple, current_target_index: int, def_color=(255, 255, 0), target_color=(0, 255, 0)):
    for i, rect in enumerate(rects):
        pygame.draw.rect(
            screen,
            target_color if i == current_target_index else def_color,
            pygame.Rect(rect))


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


def render_text(screen, text, xPos, yPos, font: pg.font.Font):
    textWithStuff = font.render(text, True, [0, 0, 0])

    textRect = textWithStuff.get_rect()
    textRect.left = xPos
    textRect.top = yPos

    screen.blit(textWithStuff, textRect)


class Button:
    def __init__(self, screen, text, image, buttonxPos, buttonyPos, width, height, func):
        super().__init__()
        self.screen = screen
        self.image = image
        self.text = text
        self.rect = pg.Rect(buttonxPos, buttonyPos, width, height)
        self.func = func
        self.font = pg.font.Font('freesansbold.ttf', 13)

        # Scale image
        imageWidth = self.image.get_width()

        scaleFactor = self.rect.width / (imageWidth + imageWidth / 2)
        image = pg.transform.scale_by(self.image, scaleFactor)

    def apply_text(self, text):
        textWithStuff = self.font.render(text, True, [0, 0, 0])

        textRect = textWithStuff.get_rect()
        textRect.centerx = self.rect.centerx
        textRect.bottom = self.rect.bottom

        self.screen.blit(textWithStuff, textRect)

    def apply_image(self):
        imageWidth = self.image.get_width()
        imageXPos = self.rect.centerx - imageWidth / 2
        imageYPos = self.rect.top + (self.rect.width - imageWidth) / 2

        self.screen.blit(self.image, [imageXPos, imageYPos])

    def update(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.func()

    def draw(self):
        pg.draw.rect(self.screen, [255, 119, 0], self.rect)
        self.apply_text(self.text)
        self.apply_image()
