from pico2d import *
import game_world
import Level1_state
import game_framework

class Bullet:
    image = None

    def __init__(self, x=90, y=90, velocity=10):
        if Bullet.image == None:
            Bullet.image = load_image('used_image/bullet_candy.png')

        self.x, self.y, self.velocity = x, y, velocity

        self.left = self.x - 20
        self.right = self.x + 20
        self.top = self.y + 20
        self.bottom = self.y - 20

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += 1000 * game_framework.frame_time

        if self.x < 25 or self.x > 1050 - 20:
            print("checking")
            Level1_state.boss_character.hp -= 2
            print(Level1_state.boss_character.hp)
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

