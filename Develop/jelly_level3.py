from pico2d import *
import random
import game_framework


class Small_Jelly_lv3:
    image = None

    def __init__(self):
        self.x, self.y = 1000, 200
        self.speed = random.randint(18, 30)
        self.frame = 0
        self.disappear_frame = 0
        self.disappeared_image = load_image('used_image/bullet_disappear.png')


        if Small_Jelly_lv3.image == None:
            Small_Jelly_lv3.image = load_image('used_image/Level3_jelly.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.disappear_frame = (self.disappear_frame + 1) % 4
        self.x -= self.speed

        if self.x <= -10:
            self.x = 1000
            if self.y == 90:
                self.y = 200
            elif self.y == 200:
                self.y = 90

    def draw(self):
        self.image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def disappear(self):
        self.disappeared_image.clip_draw(self.disappear_frame * 300, 0, 300, 300, self.x, self.y)
        self.x = 1000
        if self.y == 200:
            self.y = 90
        elif self.y == 90:
            self.y = 200



class Big_Jelly_lv3:
    image = None

    def __init__(self):
        self.x, self.y = 1000, 90
        self.speed = random.randint(10, 20)
        self.frame = 0
        self.disappear_frame = 0
        self.disappeared_image = load_image('used_image/bullet_disappear.png')

        if Big_Jelly_lv3.image == None:
            Big_Jelly_lv3.image = load_image('used_image/level3_big_bullet.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.disappear_frame = (self.disappear_frame + 1) % 4
        self.x -= self.speed
        if self.x < -10:
            self.x = 1000
            if self.y == 90:
                self.y = 200
            elif self.y == 200:
                self.y = 90

    def draw(self):
        self.image.clip_draw(self.frame * 160, 0, 160, 160, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def disappear(self):
        self.disappeared_image.clip_draw(self.disappear_frame * 300, 0, 300, 300, self.x, self.y)
        self.x = 1000
        if self.y == 200:
            self.y = 90
        elif self.y == 90:
            self.y = 200

