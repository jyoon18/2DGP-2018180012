from pico2d import *

class Aim_Up:

    def __init__(self):
        self.image = load_image('used_image/aim.png')
        self.x, self.y = 200, 200

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

class Aim_Down:
    def __init__(self):
        self.image = load_image('used_image/aim.png')
        self.x, self.y = 200, 90

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

