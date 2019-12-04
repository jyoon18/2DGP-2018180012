import game_framework
from pico2d import *
import character_select_state
import Level3_state
from map import Level3_Map


state_image = None
character14 = None
character25 = None

map_lv3 = None

class Success_Character1_State:
    def __init__(self):
        self.x, self.y = 640, 350
        self.x2, self.y2 = 900, 300
        self.frame = 0
        self.frame2 = 0
        self.image = load_image('used_image/success.png')

    def update(self):
        self.frame = (self.frame + 1) % 10


    def draw(self):
        self.image.clip_draw(self.frame * 370, 0, 370, 370, self.x, self.y, 200, 200)


class Success_Character2_State:
    def __init__(self):
        self.x, self.y = 640, 350
        self.frame = 0
        self.image = load_image('used_image/character2_success.png')

    def update(self):
        self.frame = (self.frame + 1) % 5

    def draw(self):
        self.image.clip_draw(self.frame * 370, 0, 370, 370, self.x, self.y)



def enter():

    global character14, character25, state_image, map_lv3

    character14 = Success_Character1_State()
    character25 = Success_Character2_State()
    state_image = load_image('used_image/success_state_window_Lv3.png')

    map_lv3 = Level3_Map()
    map_lv3.sbgm.play()

def exit():
    global character14, character25, state_image, map_lv3
    del character14
    del character25
    del state_image
    del map_lv3


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(Level3_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
    pass

def update():
    global character14, character2, map_lv3
    character14.update()
    character25.update()
    map_lv3.bgm.stop()

    pass

def draw():
    clear_canvas()

    state_image.draw(640, 300)
    if character_select_state.character_select_number == 1:
        character14.draw()
    elif character_select_state.character_select_number == 2:
        character25.draw()

    update_canvas()
    delay(0.1)
    pass

def pause():
    pass


def resume():
    pass






