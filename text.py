import pygame as pg

class Text:
    def __init__(self, font, size, message, antialias, colour, x, y, centered):
        self.font = pg.font.Font(font, size)
        self.render = self.font.render(message, antialias, colour)
        self.rect = self.render.get_rect()
        self.position = (x, y)
        self.centered = centered
    
    def display(self, screen):
        if self.centered:
            screen.blit(self.render, (self.position[0] - self.rect.center[0], self.position[1] - self.rect.center[1]))
        else:
            screen.blit(self.render, (self.position[0], self.position[1] - self.rect.center[1]))