from pico2d import *

class Aim_Up:

    def __init__(self):
        self.image = load_image('used_image/aim.png')
        self.x, self.y = 200, 200

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40

class Aim_Down:
    def __init__(self):
        self.image = load_image('used_image/aim.png')
        self.x, self.y = 200, 90

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40

