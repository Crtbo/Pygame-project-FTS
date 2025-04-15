import pygame as pg
import random as ry
from object import Object

class Coin(Object):
    coins = []

    def __init__(self, type, image, x, y, velocity_x, velocity_y, frames, frame_speed):
        super().__init__(type, image, x, y, velocity_x, velocity_y)
        Coin.coins.append(self)
        self.value = 1
        self.gravity = 15
        self.starting_bounce = True
        self.frames = frames
        self.len_frames = len(self.frames)
        self.frame_speed = frame_speed
        self.frame_time = pg.time.get_ticks()
        self.frame_counter = 0
        self.frames_unstarted = True

    def animate(self):
        if self.frames_unstarted or pg.time.get_ticks() - self.frame_time > self.frame_speed:
            self.frames_unstarted = False
            self.frame_time = pg.time.get_ticks()
            self.image = self.frames[self.frame_counter % self.len_frames]
            self.frame_counter += 1
    
    def collide(self, players_list, type, sound):
        if self.collision_detection(players_list, type):
            player = self.collision_detection(players_list, type)
            pg.mixer.Sound.play(sound)
            if player.money < 999: player.money += self.value
            Coin.coins.remove(self)
            del self
        
    def update(self, delta_time, screen, screen_size):
        if self.position[0] <= 0 or self.position[0] >= screen_size[0] - self.size[0]:
            self.velocity[0] *= -1
            self.position[0] += self.velocity[0] * delta_time
        
        if self.starting_bounce:
            self.velocity[1] -= ry.randint(200, 300)
            self.starting_bounce = False
        
        self.position[0] += self.velocity[0] * delta_time
        self.velocity[1] += self.gravity
        self.position[1] += self.velocity[1] * delta_time
    
        self.hitboxes = (pg.Rect(self.position[0], self.position[1], self.size[0], self.size[1]),)
        screen.blit(self.image, self.position)
