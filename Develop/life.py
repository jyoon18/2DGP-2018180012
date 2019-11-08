from pico2d import *

class Life:
    def __init__(self):
        self.x, self.y = 840, 500
        self.image = load_image('used_image/life.png')
        self.interval_distance = 60
        
    def update(self):
        self.x += self.interval_distance

    def draw(self):
        self.image.draw(self.x, self.y)