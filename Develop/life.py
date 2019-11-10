from pico2d import *

class Life:
    def __init__(self):
        self.x, self.y = 950, 540
        self.image = load_image('used_image/life.png')
        self.interval_distance = 65

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        #self.image.draw(self.x + self.interval_distance, self.y)
        #self.image.draw(self.x + self.interval_distance * 2, self.y)
        #self.image.draw(self.x + self.interval_distance * 3, self.y)
        #self.image.draw(self.x + self.interval_distance * 4, self.y)
