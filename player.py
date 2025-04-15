import pygame as pg
from object import Object

class Player(Object):
    players = []

    def __init__(self, type, image, x, y, velocity_x, velocity_y, image_moving_1, image_moving_2,bullet_image, explo_frames, explo_sfx, warn_sfx):
        super().__init__(type, image, x, y, velocity_x, velocity_y)
        Player.players.append(self)
        self.image_invu = self.image.copy()
        self.image_invu.fill((100, 100, 100, 75), special_flags=pg.BLEND_RGBA_MULT)
        self.flame_1 = image_moving_1
        self.flame_2 = image_moving_2
        self.image_moving = self.flame_1
        self.image_moving_invu = self.image_moving.copy()
        self.image_moving_invu.fill((100, 100, 100, 5), special_flags=pg.BLEND_RGBA_MULT)
        self.current_image = self.image
        self.current_image_moving = self.image_moving
        self.max_health = 1
        self.health = self.max_health
        self.lost = False
        self.invu = True
        self.flash_on = False
        self.invu_ticks = 0
        self.flash_time = pg.time.get_ticks()
        self.unflash_time = pg.time.get_ticks()
        self.money = 0
        self.level = 0
        self.levels_bool = [True, False, False]
        self.bullet_image = bullet_image
        self.bullet_damage = 1
        self.bullet_reload = 200
        self.bullet_double = False
        self.bullet_time = 0
        self.speed_boost = False
        self.fastened_v = self.velocity[0] * 2
        self.normal_v = self.velocity[0]
        self.frames = explo_frames
        self.len_frames = len(self.frames)
        self.frame_speed = 75
        self.frame_time = pg.time.get_ticks()
        self.frame_counter = 0
        self.frames_unstarted = True
        self.frames_ended = False
        self.explo_sfx = explo_sfx
        self.sound_unh = True
        self.warn_sfx = warn_sfx
        self.game_beat = False
    
    def explosion(self, screen):
        if self.lost == True:
            if self.sound_unh:
                self.sound_unh = False
                pg.mixer.Sound.play(self.explo_sfx)
            if self.frames_unstarted or pg.time.get_ticks() - self.frame_time > self.frame_speed and not(self.frames_ended):
                self.frames_unstarted = False
                self.frame_time = pg.time.get_ticks()
                self.current_frame = self.frames[self.frame_counter]
                self.frame_counter += 1
                if self.frame_counter >= self.len_frames:
                    self.frames_ended = True
            
            if not(self.frames_ended): screen.blit(self.current_frame, (self.position[0] + 5, self.position[1] - 5))
        
    def collide(self, list, type):
        if not(self.invu):
            self.current_image = self.image
            self.current_image_moving = self.image_moving
            if self.collision_detection(list, type):
                hazard = self.collision_detection(list, type)
                self.health -= 1
                if self.health <= 0:
                    self.lost = True
                self.invu = True
                self.flash_time = pg.time.get_ticks()
                if hazard.type == "enemy_bullet":
                    hazard.alive = False
                    hazard.object_hit = True
                    hazard.death_pos = hazard.position
                if hazard.type != "boss_2":
                    list.remove(hazard)
                    del hazard
        else:
            if self.invu_ticks > 5:
                self.invu_ticks = 0
                self.invu = False
            else:
                if pg.time.get_ticks() - self.flash_time > 100 and not(self.flash_on):
                    self.flash_on = True
                    self.unflash_time = pg.time.get_ticks()
                    self.current_image = self.image_invu
                    self.current_image_moving = self.image_moving_invu
                    self.invu_ticks += 1
                if self.flash_on and pg.time.get_ticks() - self.unflash_time > 200:
                    pg.mixer.Sound.play(self.warn_sfx)
                    self.flash_on = False
                    self.flash_time = pg.time.get_ticks()
                    self.current_image = self.image
                    self.current_image_moving = self.image_moving


    def update(self, delta_time, screen, screen_size):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_LSHIFT] and self.speed_boost:
            self.velocity[0] = self.fastened_v
            self.image_moving = self.flame_2
        else: 
            self.velocity[0] = self.normal_v
            self.image_moving = self.flame_1
        
        if keys[pg.K_q]: 
            self.lost = True
            self.health = 0
        
        if keys[pg.K_a] or keys[pg.K_LEFT] and keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.position[0] += 0 * delta_time
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.position[0] = max(0, self.position[0] - self.velocity[0] * delta_time)
            screen.blit(self.current_image_moving, self.position)
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.position[0] = min(screen_size[0] - self.size[0], self.position[0] + self.velocity[0] * delta_time)
            screen.blit(pg.transform.flip(self.current_image_moving, True, False), self.position)
        
        screen.blit(self.current_image, self.position)
        self.hitboxes = (pg.Rect(self.position[0] + 16, self.position[1] + 8, self.size[0] - 32, self.size[1] - 16),)
    
    def reset(self, screen_size):
        self.position = [screen_size[0] // 2 - self.image.get_width() // 2, screen_size[1] - self.image.get_height() * 1.5]
        self.lost = False
        self.invu = True
        self.health = self.max_health
        self.frames_unstarted = True
        self.frames_ended = False
        self.frame_counter = 0
        self.sound_unh = True