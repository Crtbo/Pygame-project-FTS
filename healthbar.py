import pygame as pg

class Healthbar:
    def __init__(self, health):
        self.health = health
        self.size = health
    
    def update(self, screen, screen_size):
        rect_r = pg.Rect(0, 0, self.size * 2, 30)
        rect_r.center = (screen_size[0] // 2, 35)
        pg.draw.rect(screen, (230, 58, 46), rect_r)
        rect_g = pg.Rect(rect_r.topleft[0], 20, self.health * 2, 30)
        pg.draw.rect(screen, (46, 230, 58), rect_g)
        rect_w = pg.Rect(0, 0, self.size * 2 + 8, 30)
        rect_w.center = (screen_size[0] // 2, 35)
        pg.draw.rect(screen, (217, 255, 248), rect_w, 4)
    
    def lower(self, damage):
        self.health -= damage