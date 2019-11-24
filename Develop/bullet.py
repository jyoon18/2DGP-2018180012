from pico2d import *
import game_world
import Level1_state
import Level2_state
import Level3_state
import game_framework

class Bullet:

    image = None

    def __init__(self, x=45, y=45, velocity=10):
        if Bullet.image is None:
            Bullet.image = load_image('used_image/bullet_candy.png')

        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += 900 * game_framework.frame_time

        if Level1_state.level1_state_check == 1 and self.x > 1050 - 20:
            Level1_state.boss_character.hp -= 20
            game_world.remove_object(self)

        if Level2_state.level2_state_check == 1 and self.x > 1050 - 20:
            Level2_state.boss_character.hp -= 30
            game_world.remove_object(self)

        if Level3_state.level3_state_check == 1 and self.x > 1050 - 20:
            Level2_state.boss_character.hp -= 40
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
