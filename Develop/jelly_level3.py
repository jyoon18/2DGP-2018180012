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

class Small_Jelly_lv3:
    image = None

    def __init__(self):
        self.x, self.y = 640, 200
        self.speed = random.randint(110, 120)
        self.frame = 0
        self.random = random.randint(0, 1)

        if Small_Jelly_lv3.image is None:
            Small_Jelly_lv3.image = load_image('used_image/Level3_jelly.png')

    def update(self):
        self.frame = (int(self.frame) + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.x -= self.speed * game_framework.frame_time

    def draw(self):
        self.image.clip_draw(int(self.frame) * 80, 0, 80, 80, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def disappear(self):
        self.x = 1000
        if self.random == 0:
            self.y = 90
        else:
            self.y = 200


class Big_Jelly_lv3:
    image = None

    def __init__(self):
        self.x, self.y = 1000, 90
        self.speed = random.randint(90, 100)
        self.frame = 0
        self.random = random.randint(0, 1)

        if Big_Jelly_lv3.image == None:
            Big_Jelly_lv3.image = load_image('used_image/level3_big_bullet.png')

    def update(self):
        self.frame = (int(self.frame) + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.x -= self.speed * game_framework.frame_time

    def draw(self):
        self.image.clip_draw(self.frame * 160, 0, 160, 160, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40

    def disappear(self):
        self.x = 1000
        if self.random == 0:
            self.y = 90
        else:
            self.y = 200


