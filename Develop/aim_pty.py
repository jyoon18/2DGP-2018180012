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