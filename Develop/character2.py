from pico2d import *
import game_framework

class Character2:
    def __init__(self):
        self.x, self.y = 90, 160
        self.frame = 0
        self.attack_image = load_image('used_image/character2_up_attack.png')
        self.image = load_image('used_image/character02_4.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 320, 0, 320, 320, self.x, self.y)

    def Up(self):
        self.attack_image.draw(180, 320)

    def Down(self):
        self.attack_image.draw(180, 160)


