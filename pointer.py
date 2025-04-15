import pygame as pg

class Pointer:
    def __init__(self, image):
        self.image = image
        self.size = image.get_rect()
        self.position = pg.mouse.get_pos()
        self.visibility = pg.mouse.set_visible(False)
    
    def update(self, screen):
        self.position = pg.mouse.get_pos()

        if pg.mouse.get_focused():
            screen.blit(self.image, (self.position[0] - self.size.center[0], self.position[1] - self.size.center[1]))
