from pico2d import *
import random
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPPED_KMPH = 20.0
RUN_SPPED_MPM = (RUN_SPPED_KMPH * 1000.0 / 60.0)
RUN_SPPED_MPS = (RUN_SPPED_MPM / 60.0)
RUN_SPPED_PPS = (RUN_SPPED_MPS * PIXEL_PER_METER)

TIMER_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIMER_PER_ACTION
FRAME_PER_ACTION = 2


class Small_Jelly_lv1:
    image = None

    def __init__(self):
        self.x, self.y = 640, 200
        self.speed = random.randint(100, 200)
        self.frame = 0
        self.random = random.randint(0, 1)

        if Small_Jelly_lv1.image is None:
            Small_Jelly_lv1.image = load_image('used_image/Level1_jelly.png')

    def update(self):
        self.frame = (int(self.frame) + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        self.x -= self.speed * game_framework.frame_time

    def draw(self):
        self.image.clip_draw(int(self.frame) * 80, 0, 80, 80, self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def disappear(self):
        self.x = 1000
        if self.random == 0:
            self.y = 90
        else:
            self.y = 200


class Big_Jelly_lv1:
    image = None

    def __init__(self):
        self.x, self.y = 1000, 90
        self.speed = random.randint(100, 150)
        self.frame = 0
        self.random = random.randint(0, 1)

        if Big_Jelly_lv1.image is None:
            Big_Jelly_lv1.image = load_image('used_image/big_bullet2.png')

    def update(self):
        self.frame = (int(self.frame) + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.x -= self.speed * game_framework.frame_time


    def draw(self):
        self.image.clip_draw(int(self.frame) * 160, 0, 160, 160, self.x, self.y, 110, 110)

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40

    def disappear(self):
        self.x = 1000
        if self.random == 0:
            self.y = 90
        else:
            self.y = 200
