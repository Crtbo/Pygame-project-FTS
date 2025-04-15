import pygame as pg
from object import Object

class Bullet(Object):
    bullets = []

    def __init__(self, type, image, x, y, velocity_x, velocity_y, damage):
        super().__init__(type, image, x, y, velocity_x, velocity_y)
        Bullet.bullets.append(self)
        self.damage = damage
        self.hitboxes = (pg.Rect(self.position[0], self.position[1], self.size[0], self.size[1]),)
        
    def update(self, delta_time, screen):
        self.position[0] += self.velocity[0] * delta_time
        self.position[1] += self.velocity[1] * delta_time

        self.hitboxes = (pg.Rect(self.position[0], self.position[1], self.size[0], self.size[1]),)
        screen.blit(self.image, self.position)