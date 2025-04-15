import pygame as pg
import math as my
import random as ry
from object import Object

class Enemy(Object):
    enemies = []
    spawned_num = 1
    
    def __init__(self, type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed):
        super().__init__(type, image, x, y, velocity_x, velocity_y)
        Enemy.enemies.append(self)
        Enemy.spawned_num += 1
        self.original_image = self.image.copy()
        self.white_image = self.image.copy()
        self.white_image.fill((100, 100, 100, 0), special_flags=pg.BLEND_RGBA_ADD)
        self.health = health
        self.damageable = True
        self.coin_chance = coin_chance
        self.coin_frequency = coin_frequency
        self.lose_sound = lose_sound
        self.white_time = 0
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
            self.original_image = self.image.copy()
            self.white_image = self.image.copy()
            self.white_image.fill((100, 100, 100, 0), special_flags=pg.BLEND_RGBA_ADD)
            self.frame_counter += 1

    def out_of_health(self):
        if self.health <= 0:
            pg.mixer.Sound.play(self.lose_sound)
            Enemy.enemies.remove(self)
            del self
            return True
        return False

    def collide(self, list, type, healthbar, hit_sound):
        if self.collision_detection(list, type):
            bullet = self.collision_detection(list, type)
            if self.damageable:
                self.health -= bullet.damage
                if self.health > 0: pg.mixer.Sound.play(hit_sound)
                if self.type == "boss_1" or self.type == "boss_2":
                    healthbar.lower(bullet.damage)
                self.white_time = pg.time.get_ticks()
            list.remove(bullet)
            del bullet

    def whited(self):
        if pg.time.get_ticks() - self.white_time >= 50:
            self.image = self.original_image
        else:
            self.image = self.white_image

class Follower(Enemy):
    def __init__(self, type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed):
        super().__init__(type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed)
        
    def update(self, delta_time, screen, screen_size):        
        if self.position[0] <= 0 or self.position[0] >= screen_size[0] - self.size[0]:
            self.velocity[0] *= -1
            self.position[0] += self.velocity[0] * delta_time
        
        self.position[0] += self.velocity[0] * delta_time
        self.position[1] += self.velocity[1] * delta_time

        self.hitboxes = (pg.Rect(self.position[0], self.position[1] + 8, 55, 19), pg.Rect(self.position[0] + 8, self.position[1] + 32, 39, 7), pg.Rect(self.position[0] + 16, self.position[1] + 44, 23, 3))
        screen.blit(self.image, self.position)

class Shooter(Enemy):
    def __init__(self, type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed):
        super().__init__(type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed)
        self.move_time = pg.time.get_ticks()
        self.bullet_time = pg.time.get_ticks()
        self.bullet_for = 2000
        self.bullet_allowed = True
        self.directions = ry.randint(-20, 20)
    
    def update(self, delta_time, screen, screen_size):
        if pg.time.get_ticks() - self.move_time >= 3000 or self.position[0] <= 0 or self.position[0] >= screen_size[0] - self.size[0]:
            self.velocity[0] *= -1
            self.position[0] += self.velocity[0] * delta_time
            self.move_time = pg.time.get_ticks()

        self.position[0] += self.velocity[0] * delta_time
        self.position[1] += self.velocity[1] * delta_time

        self.hitboxes = (pg.Rect(self.position[0] + 4, self.position[1], 83, 71), pg.Rect(self.position[0] + 4, self.position[1] + 72, 27, 7), pg.Rect(self.position[0] + 60, self.position[1] + 72, 27, 7))
        screen.blit(self.image, self.position)        

class Coin_Crab(Enemy):
    def __init__(self, type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed):
        super().__init__(type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed)

    def update(self, delta_time, screen, screen_size):
        if self.position[0] <= 0 or self.position[0] >= screen_size[0] - self.size[0]:
            self.velocity[0] *= -1
            self.position[0] += self.velocity[0] * delta_time

        self.position[0] += self.velocity[0] * delta_time
        self.position[1] += self.velocity[1] * delta_time
        
        self.hitboxes = (pg.Rect(self.position[0] + 4, self.position[1] + 4, 23, 23), pg.Rect(self.position[0], self.position[1] + 8, 31, 11))
        screen.blit(self.image, self.position)

class The_invader(Enemy):
    def __init__(self, type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed):
        super().__init__(type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed)
        self.bullet_time = pg.time.get_ticks()
        self.bullet_for = 2000
        self.damageable = False
        self.wave_time = 0

    def update(self, delta_time, screen, screen_size):
        if self.position[0] <= 50 or self.position[0] >= screen_size[0] - self.size[0] - 50:
            self.velocity[0] *= -1
            self.position[0] += self.velocity[0] * delta_time
        
        if self.position[1] <= 150:
            self.position[1] += self.velocity[1] * delta_time
            self.damageable = False
        else:
            self.position[1] += my.sin(self.wave_time) * 1.2
            self.wave_time += delta_time
            self.position[0] += self.velocity[0] * delta_time
            self.damageable = True
        
        self.hitboxes = (pg.Rect(self.position[0], self.position[1] + 89, 27, 41), pg.Rect(self.position[0] + 24, self.position[1] + 68, 15, 27), pg.Rect(self.position[0] + 40, self.position[1] + 48, 151, 83), pg.Rect(self.position[0] + 192, self.position[1] + 64, 15, 31), pg.Rect(self.position[0] + 24, self.position[1] + 68, 15, 27), pg.Rect(self.position[0] + 40, self.position[1] + 48, 151, 83), pg.Rect(self.position[0] + 208, self.position[1] + 96, 27, 39))
        screen.blit(self.image, self.position)

class Swayer(Enemy):
    def __init__(self, type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed):
        super().__init__(type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed)
        self.st_position = self.position[1]
        self.swaying = False
    
    def update(self, delta_time, screen, screen_size):
        if self.position[0] < 50 or self.position[0] > screen_size[0] - self.size[0] - 50:
            self.st_position = self.position[1]
            self.swaying = False
            self.velocity[0] *= -1
            self.position[0] += self.velocity[0] * delta_time
        
        if not(self.swaying):
            self.position[1] += self.velocity[1] * delta_time
            if self.position[1] - self.st_position > 150:
                self.swaying = True
        else:
            self.position[0] += self.velocity[0] * delta_time

        self.hitboxes = (pg.Rect(self.position[0] + 4, self.position[1] + 12, 79, 67),)
        screen.blit(self.image, self.position)

class Stopper(Enemy):
    def __init__(self, type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed):
        super().__init__(type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed)
        self.stopped = False
        self.running_for = ry.randint(2000, 4000)
        self.running_time = pg.time.get_ticks()
        self.stop_time = pg.time.get_ticks()
        self.bullet_time = pg.time.get_ticks()
        self.bullet_for = 300
        self.bullet_allowed = False
    
    def update(self, delta_time, screen, screen_size):
        if self.position[0] <= 250 or self.position[0] >= screen_size[0] - self.size[0] - 250:
            self.velocity[0] *= -1
            self.position[0] += self.velocity[0] * delta_time
        
        if pg.time.get_ticks() - self.running_time > self.running_for and not(self.stopped):
            self.running_for = ry.randint(2000, 4000)
            self.stopped = True
            self.stop_time = pg.time.get_ticks()
            self.bullet_allowed = True
        self.directions = ry.choice((-400, -200, 0, 200, 400))

        if self.stopped and pg.time.get_ticks() - self.stop_time > 2000:
            self.stopped = False
            self.running_time = pg.time.get_ticks()
            self.bullet_allowed = False
        
        if not(self.stopped):
            self.position[0] += self.velocity[0] * delta_time
            self.position[1] += self.velocity[1] * delta_time

        self.hitboxes = (pg.Rect(self.position[0] + 4, self.position[1], 83, 71), pg.Rect(self.position[0] + 4, self.position[1] + 72, 27, 7), pg.Rect(self.position[0] + 60, self.position[1] + 72, 27, 7))
        screen.blit(self.image, self.position)        

class The_demon(Enemy):
    def __init__(self, type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed):
        super().__init__(type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed)
        self.damageable = False
        self.enemy_time = pg.time.get_ticks()
        self.enemy_for = 4000
    
    def update(self, delta_time, screen, screen_size):
        if self.position[1] <= 150 and not(self.damageable):
            self.position[1] += 100 * delta_time
            self.damageable = False
        else:
            if self.position[0] <= 0 or self.position[0] >= screen_size[0] - self.size[0]:
                self.velocity[0] *= -1
                self.position[0] += self.velocity[0] * delta_time
            if self.position[1] <= 0 or self.position[1] >= screen_size[1] - self.size[1]:
                self.velocity[1] *= -1
                self.position[1] += self.velocity[1] * delta_time

            self.position[0] += self.velocity[0] * delta_time
            self.position[1] += self.velocity[1] * delta_time
            self.damageable = True
            
        self.hitboxes = (pg.Rect(self.position[0], self.position[1] + 64, 191, 59), pg.Rect(self.position[0] + 48, self.position[1] + 8, 103, 167), pg.Rect(self.position[0] + 12, self.position[1], 35, 163), pg.Rect(self.position[0] + 144, self.position[1], 35, 163))
        screen.blit(self.image, self.position)

class The_robot(Enemy):
    def __init__(self, type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed, arms):
        super().__init__(type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed)
        self.hitboxes = (pg.Rect(self.position[0] + 28, self.position[1], 399, 135), pg.Rect(self.position[0] + 88, self.position[1] + 144, 279, 27))
        self.arms = arms
        self.bullet_time = pg.time.get_ticks()
        self.bullet_for = 2000
        self.enemy_time = pg.time.get_ticks()
        self.enemy_for = 5000
        self.damageable = False
        self.wave_time = 0
    
    def update(self, delta_time, screen):
        if self.position[1] <= -25 and not(self.damageable):
            self.position[1] += self.velocity[1] * delta_time
            self.damageable = False
        else:
            self.position[1] += my.sin(self.wave_time) * 0.2
            self.position[0] += my.cos(self.wave_time) * 0.5
            self.wave_time += delta_time
            self.damageable = True
    
        self.hitboxes = (pg.Rect(self.position[0] + 28, self.position[1], 399, 135), pg.Rect(self.position[0] + 88, self.position[1] + 144, 279, 27))
        screen.blit(self.image, self.position)
        screen.blit(self.arms[0], (self.position[0] - 125, self.position[1]))
        screen.blit(self.arms[1], (self.position[0] + 475, self.position[1]))

class Bot(Enemy):
    def __init__(self, type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed):
        super().__init__(type, image, x, y, velocity_x, velocity_y, health, coin_chance, coin_frequency, lose_sound, frames, frame_speed)
        self.st_position = self.position[1]
        self.start = True

    def update(self, delta_time, screen, screen_size):
        if self.position[0] <= 0 or self.position[0] >= screen_size[0] - self.size[0]:
            self.velocity[0] *= -1
            self.position[0] += self.velocity[0] * delta_time
        
        if self.start:
            self.position[1] += self.velocity[1] * delta_time
            if self.position[1] - self.st_position > 75:
                self.start = False
        else:
            self.position[0] += self.velocity[0] * delta_time
            self.position[1] += self.velocity[1] * delta_time

        self.hitboxes = (pg.Rect(self.position[0] + 4, self.position[1] + 4, 43, 35),)
        screen.blit(self.image, self.position)