from pico2d import *
import game_framework


class Level1_Map:
    def __init__(self):
        self.image = load_image('used_image/map03_3.png')
        self.image2 = load_image('used_image/map03_3.png')
        self.x, self.y = 640, 300
        self.frame = 0
        self.velocity = 100

    def update(self):
        self.x -= self.velocity * game_framework.frame_time
        if self.x <= 0:
            self.x = 640

    def draw(self):
        self.image.draw(self.x, self.y)


class Level2_Map:
    def __init__(self):
        self.image = load_image('used_image/map02_4.png')
        self.image2 = load_image('used_image/map02_4.png')

        self.x, self.y = 640, 300
        self.frame = 0

    def update(self):
        self.x -= 1
        if self.x == 0:
            self.x = 640

    def draw(self):
        self.image.draw(self.x, self.y)

class Level3_Map:
    def __init__(self):
        self.image = load_image('used_image/map04.png')
        self.image2 = load_image('used_image/map04.png')
        self.x, self.y = 640, 300
        self.frame = 0

    def update(self):
        self.x -= 1
        if self.x == 0:
            self.x = 640

    def draw(self):
        self.image.draw(self.x, self.y)