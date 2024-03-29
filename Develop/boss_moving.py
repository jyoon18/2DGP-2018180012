from pico2d import *
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPPED_KMPH = 20.0
RUN_SPPED_MPM = (RUN_SPPED_KMPH * 1000.0 / 60.0)
RUN_SPPED_MPS = (RUN_SPPED_MPM / 60.0)
RUN_SPPED_PPS = (RUN_SPPED_MPS * PIXEL_PER_METER)

TIMER_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIMER_PER_ACTION
FRAME_PER_ACTION = 3

class Level1_Boss:

    def __init__(self):
        self.x, self.y = 1050, 150
        self.frame = 0
        self.hp = 100
        self.font = load_font('ENCR10B.TTF', 35)
        self.image = load_image('used_image/boss.png')

    def update(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    def draw(self):
        self.image.clip_draw(int(self.frame) * 316, 0, 290, 230, self.x, self.y)
        self.font.draw(self.x - 90, self.y + 100, 'HP: %d' % self.hp, (255, 0, 0))

class Level2_Boss:

    def __init__(self):
        self.x, self.y = 1050, 150
        self.frame = 0
        self.hp = 300
        self.font = load_font('ENCR10B.TTF', 35)
        self.image = load_image('used_image/boss.png')

    def update(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    def draw(self):
        self.image.clip_draw(int(self.frame) * 316, 0, 290, 230, self.x, self.y)
        self.font.draw(self.x - 90, self.y + 100, 'HP: %d' % self.hp, (255, 0, 0))

class Level3_Boss:

    def __init__(self):
        self.x, self.y = 1050, 150
        self.frame = 0
        self.hp = 600
        self.font = load_font('ENCR10B.TTF', 35)
        self.image = load_image('used_image/boss.png')

    def update(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    def draw(self):
        self.image.clip_draw(int(self.frame) * 316, 0, 290, 230, self.x, self.y)
        self.font.draw(self.x - 90, self.y + 100, 'HP: %d' % self.hp, (255, 0, 0))
