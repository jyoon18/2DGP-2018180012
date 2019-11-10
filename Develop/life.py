from pico2d import *
import game_world

class Life:
    def __init__(self):
        self.x, self.y = 950, 540
        self.image = load_image('used_image/life.png')
        self.interval_distance = 65
    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def remove(self):
        game_world.remove_object(self)