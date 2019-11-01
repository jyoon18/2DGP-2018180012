from pico2d import *

class Maps:
    def __init__(self):
        self.image = load_image('map02_3.png')
        self.x, self.y = 640,300
        self.frame = 0
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x -= 1
