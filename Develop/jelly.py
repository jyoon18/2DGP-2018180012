from pico2d import *

class Small_Jelly_lv1:
    def __init__(self):
        self.x, self.y = 1000, 0
        self.speed = 0
        self.image = load_image('Level1_jelly.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 3

    def draw(self):
        self.image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)

class Big_Jelly_lv1:
    def __init__(self):
        self.x, self.y = 0, 0
        self.speed = 0
        self.image = load_image('big_bullet.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 160, 0, 160, 160, self.x, self.y)