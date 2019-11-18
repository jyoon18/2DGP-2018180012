from pico2d import *
import game_world


class Bullet:
    image = None
    def __init__(self, x = 400, y = 300, velocity = 1):
        if Bullet.image == None:
            Bullet.image = load_image('used_image/bullet_candy.png')
            self.x, self.y, self.velocity = x, y, velocity

    def update(self):
        self.x += self.velocity

        if self.x > 1280 - 40:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)