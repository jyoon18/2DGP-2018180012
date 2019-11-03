from pico2d import *

class Boss:
    def __init__(self):
        self.x, self.y = 1050, 200
        self.frame = 0
        self.image = load_image('used_image/boss.png')

    def update(self):
        self.frame = (self.frame + 1) % 3

    def draw(self):
        self.image.clip_draw(self.frame * 316, 0, 290, 230, self.x, self.y)