from pico2d import *

class Aim:
    def __init__(self):
        self.image = load_image('used_image/aim.png')
        self.x, self.y = 0,0

    def draw(self):
        self.image.draw(200, 200)
        self.image.draw(200, 90)

    def update(self):
        pass

    def get_bb_up(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def get_bb_down(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
