import game_framework
from pico2d import *
import character_select_state
from map import Level1_Map
from map import Level2_Map
from map import Level3_Map

state_image = None

character12 = None
character23 = None

maps1 = None
maps2 = None
maps3 = None

class Fail_Character1_State:
    def __init__(self):
        self.x, self.y = 640, 350
        self.frame = 0
        self.image = load_image('used_image/fail.png')

    def update(self):
        self.frame = (self.frame + 1) % 10

    def draw(self):
        self.image.clip_draw(self.frame * 370, 0, 370, 370, self.x, self.y, 300, 300)

class Fail_Character2_State:
    def __init__(self):
        self.x, self.y = 640, 350
        self.frame = 0
        self.image = load_image('used_image/character2_failed2.png')

    def update(self):
        self.frame = (self.frame + 1) % 11

    def draw(self):
        self.image.clip_draw(self.frame * 370, 0, 370, 370, self.x, self.y)

def enter():

    global character12, character23, state_image, maps1, maps2, maps3

    character12 = Fail_Character1_State()
    character23 = Fail_Character2_State()
    state_image = load_image('used_image/failure_state_window.png')
    maps1 = Level1_Map()
    maps2 = Level2_Map()
    maps3 = Level3_Map()

    maps1.fbgm.play()
    maps2.fbgm.play()
    maps3.fbgm.play()

def exit():
    global character12, character23, state_image, maps1, maps2, maps3
    del character12
    del character23
    del state_image
    del maps1
    del maps2
    del maps3

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(character_select_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
    pass

def update():
    global character12, character23, maps1, maps2, maps3
    maps1.bgm.stop()
    maps2.bgm.stop()
    maps3.bgm.stop()
    character12.update()
    character23.update()

    pass

def draw():
    clear_canvas()

    state_image.draw(640, 300)
    if character_select_state.character_select_number == 1:
        character12.draw()
    elif character_select_state.character_select_number == 2:
        character23.draw()

    update_canvas()
    delay(0.1)
    pass

def pause():
    pass


def resume():
    pass






