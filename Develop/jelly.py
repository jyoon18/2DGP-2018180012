from pico2d import *
import random

class Small_Jelly_lv1:
    def __init__(self):
        self.x, self.y = 1000, 200
        self.speed = 24
        self.image = load_image('Level1_jelly.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x -= self.speed

    def draw(self):
        self.image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)

class Big_Jelly_lv1:
    def __init__(self):
        self.x, self.y = 1000, 90
        self.speed = 12
        self.image = load_image('big_bullet2.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x -= self.speed

    def draw(self):
        self.image.clip_draw(self.frame * 160, 0, 160, 160, self.x, self.y)