from pico2d import *

import game_framework
import Level1_state
import title_state
from map import Ready

image = None
character1 = None
character2 = None

character_select_number = 0
Cbgm = None

class Select_Character1:
    def __init__(self):
        self.x, self.y = 400, 200
        self.frame = 0
        self.image = load_image('used_image/character1_select_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 168, 0, 160, 160, self.x, self.y)

class Select_Character2:
    def __init__(self):
        self.x, self.y = 800, 300
        self.frame = 0
        self.image = load_image('used_image/character2_select_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 363, 0, 363, 363, self.x, self.y)


def enter():
    global image, character1, character2, Cbgm
    image = load_image('used_image/character_select_window.png')
    character1 = Select_Character1()
    character2 = Select_Character2()
    Cbgm = Ready()
    Cbgm.tbgm.play()

def exit():
    global image, character1, character2, Cbgm
    del character1
    del character2
    del image
    del Cbgm


def handle_events():
    global character_select_number
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
                character_select_number = 1
                game_framework.change_state(Level1_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
                character_select_number = 2
                game_framework.change_state(Level1_state)

def update():
    global character1, character2
    character1.update()
    character2.update()
    pass

def draw():
    global character_state_total_time
    clear_canvas()
    image.draw(640, 300)

    character1.draw()
    character2.draw()

    update_canvas()
    delay(0.1)
    pass

