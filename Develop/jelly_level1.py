from pico2d import *
import random
import game_framework


class Small_Jelly_lv1:
    image = None

    def __init__(self):
        self.x, self.y = 1000, 200
        self.speed = random.randint(1, 5)
        self.frame = 0
        if Small_Jelly_lv1.image == None:
            Small_Jelly_lv1.image = load_image('used_image/Level1_jelly.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x -= self.speed

        if self.x <= -10:
            self.x = 1000
            if self.y == 90:
                self.y = 200
            elif self.y == 200:
                self.y = 90

    def draw(self):
        self.image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40


class Big_Jelly_lv1:
    image = None

    def __init__(self):
        self.x, self.y = 1000, 90
        self.speed = random.randint(5, 8)
        self.frame = 0
        self.random_select = random.randint(0, 1)

        if Big_Jelly_lv1.image == None:
            Big_Jelly_lv1.image = load_image('used_image/big_bullet2.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x -= self.speed
        if self.x < -10:
            self.x = 1000
            if self.y == 90:
                self.y = 200
            elif self.y == 200:
                self.y = 90

    def draw(self):
        self.image.clip_draw(self.frame * 160, 0, 160, 160, self.x, self.y)

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40
