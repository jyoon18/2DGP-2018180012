import game_framework
from pico2d import *
import character_select_state


name = "TitleState"
image_character1 = None
image_character2 = None

character1 = None
character2 = None

class Fail_Character1_State:
    def __init__(self):
        self.x, self.y = 640, 300
        self.frame = 0
        self.image = load_image('used_image/fail.png')

    def update(self):
        self.frame = (self.frame + 1) % 10

    def draw(self):
        self.image.clip_draw(self.frame * 370, 0, 370, 370, self.x, self.y)

class Fail_Character2_State:
    def __int__(self):
        self.x, self.y = 640, 300
        self.frame = 0
        self.image = load_image('used_image/')

def enter():
    global character1, character2

    character1 = Fail_Character1_State()



def exit():
    global image_character1
    del(image_character1)
    pass


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

def draw():
    clear_canvas()
    image_character1.draw(640, 300)
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass






