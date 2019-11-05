from pico2d import *
import random
import game_framework


class Small_Jelly_lv1:
    image = None

    def __init__(self):
        self.x, self.y = 1000, 200
        self.speed = random.randint(5, 10)
        self.frame = 0
        if Small_Jelly_lv1.image == None:
            Small_Jelly_lv1.image = load_image('used_image/Level1_jelly.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x -= self.speed
        if self.x == -100:
            self.x, self.y = 1000, 200

    def draw(self):
        self.image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)

class Big_Jelly_lv1:
    def __init__(self):
        self.x, self.y = 1000, 90
        self.speed = 12
        self.image = load_image('used_image/big_bullet2.png')
        self.frame = 0
        self.count_check = 50

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x -= self.speed

    def draw(self):
        self.image.clip_draw(self.frame * 160, 0, 160, 160, self.x, self.y)

