import game_framework
from pico2d import *
import character_select_state
import Level2_state
from map import Level1_Map


state_image = None

character1 = None
character2 = None

class Success_Character1_State:
    def __init__(self):
        self.x, self.y = 300, 350
        self.x2, self.y2 = 900, 300
        self.frame = 0
        self.frame2 = 0
        self.image = load_image('used_image/success.png')
        self.boss_disappear = load_image('used_image/boss_disappear.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.frame2 = (self.frame2 + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 370, 0, 370, 370, self.x, self.y, 200, 200)
        self.boss_disappear.clip_draw(self.frame2 * 300, 0, 300, 300, self.x2, self.y2)


class Success_Character2_State:
    def __init__(self):
        self.x, self.y = 300, 350
        self.x2, self.y2 = 900, 300
        self.frame = 0
        self.frame2 = 0
        self.image = load_image('used_image/character2_success.png')
        self.boss_disappear = load_image('used_image/boss_disappear.png')

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.frame2 = (self.frame2 + 1) % 8


    def draw(self):
        self.image.clip_draw(self.frame * 370, 0, 370, 370, self.x, self.y)
        self.boss_disappear.clip_draw(self.frame2 * 300, 0, 300, 300, self.x2, self.y2)

class Success_Sound:
    def __init__(self):
        self.bgm = load_music('success_effect.mp3')

def enter():

    global character1, character2, state_image, maps

    character1 = Success_Character1_State()
    character2 = Success_Character2_State()
    state_image = load_image('used_image/success_state_window_Lv1.png')
    maps = Level1_Map()

def exit():
    global character1, character2, state_image
    del character1
    del character2
    del state_image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(Level2_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
    pass

def update():
    global character1, character2, maps
    maps.bgm.stop()

    character1.update()
    character2.update()

    pass

def draw():
    clear_canvas()

    state_image.draw(640, 300)
    if character_select_state.character_select_number == 1:
        character1.draw()
    elif character_select_state.character_select_number == 2:
        character2.draw()

    update_canvas()
    delay(0.1)
    pass

def pause():
    pass


def resume():
    pass






