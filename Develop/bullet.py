from pico2d import *
import game_world
import Level1_state

class Bullet:
    image = None

    def __init__(self, x = 90, y = 90, velocity = 10):
        if Bullet.image == None:
            Bullet.image = load_image('used_image/bullet_candy.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity * 5
        if self.x < 25 or self.x > 1280 - 40:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
