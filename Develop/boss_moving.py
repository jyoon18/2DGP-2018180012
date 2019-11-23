from pico2d import *
import Level1_state

class Level1_Boss:
    def __init__(self):
        self.x, self.y = 1050, 150
        self.frame = 0
        self.hp = 100
        self.font = load_font('ENCR10B.TTF', 35)
        self.image = load_image('used_image/boss.png')

        #self.left = self.x - 95
        #self.right = self.x + 95
        #self.top = self.y + 95
        #self.bottom = self.y -95

    def update(self):
        self.frame = (self.frame + 1) % 3

    def draw(self):
        self.image.clip_draw(self.frame * 316, 0, 290, 230, self.x, self.y)
        self.font.draw(self.x - 45, self.y + 45, '(HP: %d)' % self.hp, (0, 0, 0))
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 95, self.y -95, self.x + 95, self.y + 95






