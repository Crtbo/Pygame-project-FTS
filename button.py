import pygame as pg

class Button:
    def __init__(self, id, image, x, y, rect, scale):
        self.id = id
        self.image = image
        self.scaled_image = pg.transform.scale(self.image, scale)
        self.scaled_image.fill((25, 25, 25, 0), special_flags=pg.BLEND_RGBA_ADD)
        self.position = [x, y]
        self.rect = rect
        self.scaled_rect = self.scaled_image.get_rect()
        self.other_rect = pg.rect.Rect(self.position[0] - self.rect.center[0], self.position[1] - self.rect.center[1], self.image.get_width(), self.image.get_height())
        self.hover = False
        self.clicked = False
        self.played = False
        
    def display(self, screen, texts):
        if self.hover:
            if type(texts) is tuple: 
                for text in texts:
                    text.display(screen)
            elif texts is not None:
                texts.display(screen)
            screen.blit(self.scaled_image, (self.position[0] - self.scaled_rect.center[0], self.position[1] - self.scaled_rect.center[1]))
        else:
            screen.blit(self.image, (self.position[0] - self.rect.center[0], self.position[1] - self.rect.center[1]))

    def detection(self, pointer, sound):
        if self.other_rect.collidepoint(pointer.position):
            self.hover = True
            if not(self.played):
                pg.mixer.Sound.play(sound)
                self.played = True
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                    self.clicked = True
                else:
                    self.clicked = False
        else:
            self.hover = False
            self.played = False

    def reset(self):
        self.clicked = False

class Upgrade(Button):
    def __init__(self, id, image, bought_image, x, y, rect, scale, cost):
        super().__init__(id, image, x, y, rect, scale)
        self.unbought_image = self.image
        self.bought_image = bought_image
        self.bought_image.fill((150, 150, 150, 150), special_flags=pg.BLEND_RGBA_MULT)
        self.cost = cost
        self.owned = False

    def detection(self, pointer, sound, money):
        if self.other_rect.collidepoint(pointer.position) and not(self.owned):
            self.hover = True
            if not(self.played):
                pg.mixer.Sound.play(sound)
                self.played = True
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP and event.button == 1 and money >= self.cost:
                    self.clicked = True
                else:
                    self.clicked = False
        else:
            self.hover = False
            self.played = False
    
    def bought(self):
        self.image = self.bought_image
        self.clicked = False
        self.owned = True
    
    def reset(self):
        self.image = self.unbought_image
        self.clicked = False
        self.owned = False
