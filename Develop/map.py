from pico2d import *

class Maps:
    def __init__(self):
        self.image_first = load_image('used_image/map02_3.png')
        self.image_second = load_image('used_image/map02_4.png')
        self.x, self.y = 640, 300
        self.frame = 0

    def update(self):
        self.x -= 1
        if self.x == 0:
            self.x = 640


    def draw(self):
        self.image_first.draw(self.x, self.y)
        if self.x == 0:
            self.image_second(self.x, self.y)