from pico2d import *
import game_framework
import game_world

# character event

F_DOWN, F_UP, J_DOWN, J_UP = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_f): F_DOWN,
    (SDL_KEYUP, SDLK_f): F_UP,
    (SDL_KEYDOWN, SDLK_j): J_DOWN,
    (SDL_KEYUP, SDLK_j): J_UP
}

class Character1:
    def __init__(self):
        self.x, self.y = 90, 90
        self.frame = 0
        self.attack_image = load_image('used_image/up_attack.png')
        self.image = load_image('used_image/running1.png')

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 160, 0, 160, 160, self.x, self.y)

    def Up(self):
        self.attack_image.draw(180, 200)

    def Down(self):
        self.attack_image.draw(180, 90)


