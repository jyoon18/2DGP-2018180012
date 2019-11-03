from pico2d import *
import random

class Small_Jelly_lv1:
    def __init__(self):
        self.x, self.y = 0, 0
        self.speed = 24
        self.image = load_image('used_image/Level1_jelly.png')
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
        self.image = load_image('used_image/big_bullet2.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x -= self.speed

    def draw(self):
        self.image.clip_draw(self.frame * 160, 0, 160, 160, self.x, self.y)




def draw_curve(p1, p2, p3, p4):
    for i in range(0, 50, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]

    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (-3 * t ** 3 + 4 * t ** 2 + t) *
         p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (-3 * t ** 3 + 4 * t ** 2 + t) *
         p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2

    for i in range(50, 100, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p2[0] + (-4 * t ** 2 + 4 * t) * p3[0] + (2 * t ** 2 - t) * p4[0]
        y = (2 * t ** 2 - 3 * t + 1) * p2[1] + (-4 * t ** 2 + 4 * t) * p3[1] + (2 * t ** 2 - t) * p4[1]
