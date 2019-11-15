from pico2d import *
import random
import game_framework


class Small_Jelly_lv2:
    image = None

    def __init__(self):
        self.x, self.y = 1000, 200
        self.speed = random.randint(6, 18)
        self.frame = 0
        self.disappear_frame = 0
        self.disappeared_image = load_image('used_image/bullet_disappear.png')

        if Small_Jelly_lv2.image == None:
            Small_Jelly_lv2.image = load_image('used_image/Level2_jelly.png')

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
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def disappear(self):
        self.disappeared_image.clip_draw(self.disappear_frame * 300, 0, 300, 300, self.x, self.y)
        self.x = 1000
        if self.y == 200:
            self.y = 90
        elif self.y == 90:
            self.y = 200


class Big_Jelly_lv2:
    image = None

    def __init__(self):
        self.x, self.y = 1000, 90
        self.speed = random.randint(6, 10)
        self.frame = 0
        self.disappear_frame = 0
        self.disappeared_image = load_image('used_image/bullet_disappear.png')

        if Big_Jelly_lv2.image == None:
            Big_Jelly_lv2.image = load_image('used_image/big_bullet2.png')

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
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def disappear(self):
        self.disappeared_image.clip_draw(self.disappear_frame * 300, 0, 300, 300, self.x, self.y)
        self.x = 1000
        if self.y == 200:
            self.y = 90
        elif self.y == 90:
            self.y = 200
